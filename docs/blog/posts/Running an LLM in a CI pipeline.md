---
title: Running an LLM in a CI pipeline
date:
  created: 2025-02-05
authors:
  - jeremy
tags:
  - github
  - github actions
  - gitlab
  - gitlab ci
  - llm
  - ai
  - ci/cd
---
# Running an LLM in a CI pipeline

## Overview

With the recent explosion of AI and large language models (LLM), I've been brainstorming how to take advantage of AI capabilities within a CI/CD pipeline.

Most of the major AI providers have a REST API, so I could of course easily use that in a CI pipeline, but there are many situations where this isn't an option:

  - **Cost**: As many "AI wrapper" companies quickly discovered, [these APIs are _expensive_](https://medium.com/@sphinxshivraj/how-much-does-ai-cost-a-comprehensive-guide-4e5836ad4e44). And running queries in a CI pipeline that could run potentially hundreds of times per day adds up quickly.
  - **Security**: Many organizations handling sensitive or proprietary data don't want their information sent to a third party like OpenAI or Google.

To solve these issues, I wanted to see if it's possible to run an LLM _locally_ in a CI job, to which I can send queries without worrying about API cost or revealing sensitive data.

## How it's done

### Tools

All the tools I'm using in this article are free to use.

| Name | Description |
| --- | --- |
| [Ollama](https://ollama.com/) | A free, open-source tool for running LLMs locally |
| [Gitlab CI](https://docs.gitlab.com/ee/ci/) | A free CI/CD pipeline system developed by Gitlab for running automated jobs in the same environment as your git repository |
| [GitHub Actions](https://github.com/features/actions) | Same as Gitlab CI, but provided by GitHub |

!!! note

    In this article I won't be getting too deep into exactly what Ollama is and how it works. To learn more about it, check out their [GitHub](https://github.com/ollama/ollama).

### Setup

To start, you'll need either a [GitHub](https://github.com) or [Gitlab](https://gitlab.com) account and you'll need to create your first repository[^1][^2]. Once that's done, create a basic CI/CD pipeline--we'll name it `ci`:

=== "GitHub Actions - `.github/workflows/ci.yml`"

    ```yaml
    name: ci
    on:
      push:
    ```

=== "Gitlab CI - `.gitlab-ci.yml`"

    ```yaml
    workflow:
      name: ci
    ```

This creates a basic structure for a pipeline that runs on all commits. To limit the pipeline to only run on a certain branch, modify GitHub's [`on.push`](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#onpushbranchestagsbranches-ignoretags-ignore) option, or Gitlab's [`workflow:rules`](https://docs.gitlab.com/ee/ci/yaml/#workflowrules). For example:

=== "GitHub Actions"

    ```yaml
    name: ci
    on:
      push:
        branches:
          - main
    ```

=== "Gitlab CI"

    ```yaml
    workflow:
      name: ci
      rules:
        - if: $CI_COMMIT_BRANCH == 'main'
    ```

### Run an LLM in a job

The `ollama` CLI is great for running a local, interactive chat session in your terminal. But for a non-interactive, automated CI job it's best to interface with the [Ollama API](https://github.com/ollama/ollama/blob/main/docs/api.md). To do this, we need to first define our `ollama` job and run Ollama as a service[^3][^4] accessible by our job.

=== "GitHub Actions"

    ```yaml
    jobs:
      ollama:
        runs-on: ubuntu-latest
        services:
          ollama: ollama/ollama
    ```

=== "Gitlab CI"

    ```yaml
    ollama:
      services:
        - image: ollama/ollama
          alias: ollama
    ```

Next we'll add our script. When we request a response from the LLM we'll need to specify a large language model to generate that response. These models can be found in [Ollama's library](https://ollama.com/library). Any model will work, but keep in mind that models with more parameters--while providing much better responses--are much larger in size. The [671 billion parameter version of `deepseek-r1`](https://ollama.com/library/deepseek-r1:671b), for example, is 404GB in size. As such, it's ideal to use smaller models such as Meta's [`llama3.2`](https://ollama.com/library/llama3.2).

Prior to generating a response, we'll first need to pull the model we want using Ollama's [`pull`](https://github.com/ollama/ollama/blob/main/docs/api.md#pull-a-model) API. Then we generate the response with the [`generate`](https://github.com/ollama/ollama/blob/main/docs/api.md#generate-a-completion) API. Any Docker image will work for this job as long as it has the ability to send web requests with tools like [`wget`](https://www.gnu.org/software/wget/) or [`curl`](https://curl.se/). For this example we'll be using `curl` with the [`alpine/curl`](https://hub.docker.com/r/alpine/curl) image.

=== "GitHub Actions"

    ```yaml
    container: alpine/curl
    steps:
      - name: Generate response
        run: |
          curl -sS -X POST -d '{"model":"llama3.2","stream":false}' ollama:11434/api/pull
          curl -sS -X POST -d '{"model":"llama3.2","stream":false,"prompt":"Hello world"}' ollama:11434/api/generate
    ```

=== "Gitlab CI"

    ```yaml
    image: alpine/curl
    script: |
      curl -sS -X POST -d '{"model":"llama3.2","stream":false}' ollama:11434/api/pull
      curl -sS -X POST -d '{"model":"llama3.2","stream":false,"prompt":"Hello world"}' ollama:11434/api/generate
    ```

??? note

    Ideally, the `pull` and `generate` operations would run in separate steps. GitHub uses the [`steps`](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#jobsjob_idsteps) functionality for this, however, the comparable functionality in Gitlab ([`run`](https://docs.gitlab.com/ee/ci/yaml/#run)) is still in the experimental stage. For simplicity for the sake of this article, we'll be running the commands in a single script in both GitHub and Gitlab. To accomplish the same in separate steps would look like this:

    === "GitHub Actions"

        ```yaml
        container: alpine/curl
        steps:
          - name: Pull model
            run: curl -sS -X POST -d '{"model":"llama3.2","stream":false}' ollama:11434/api/pull

          - name: Generate response
            run: curl -sS -X POST -d '{"model":"llama3.2","stream":false,"prompt":"Hello world"}' ollama:11434/api/generate
        ```

    === "Gitlab CI"

        ```yaml
        image: alpine/curl
        run:
          - name: Pull model
            script: curl -sS -X POST -d '{"model":"llama3.2","stream":false}' ollama:11434/api/pull

          - name: Generate response
            script: curl -sS -X POST -d '{"model":"llama3.2","stream":false,"prompt":"Hello world"}' ollama:11434/api/generate
        ```

That's all we need--let's see the response:

```
> curl -sS -X POST -d '{"model":"llama3.2","stream":false}' ollama:11434/api/pull
{"status":"success"}
> curl -sS -X POST -d '{"model":"llama3.2","stream":false,"prompt":"Hello world"}' ollama:11434/api/generate
{"model":"llama3.2","created_at":"2025-02-06T18:46:52.362892453Z","response":"Hello! It's nice to meet you. Is there something I can help you with or would you like to chat?","done":true,"done_reason":"stop","context":[128004,9125,128007,276,39766,3303,33025,2696,22,8790,220,2366,11,271,128009,128006,882,128007,271,9906,1917,128009,128006,78191,128007,271,9906,0,1102,596,6555,311,3449,499,13,2209,1070,2555,358,649,1520,499,449,477,1053,499,1093,311,6369,30],"total_duration":9728821911,"load_duration":2319403269,"prompt_eval_count":27,"prompt_eval_duration":3406000000,"eval_count":25,"eval_duration":4001000000}
```

### Parse the output

This is great, but the JSON output is a bit verbose. We can simplify the response and make it a bit more readable using the [`jq`](https://jqlang.org/) command.

=== "GitHub Actions"

    ```yaml
    steps:
      - name: Install jq
        run: apk add jq
      - name: Generate response
        run: |
          curl -sS -X POST -d '{"model":"llama3.2","stream":false}' ollama:11434/api/pull | jq -r .status
          curl -sS -X POST -d '{"model":"llama3.2","stream":false,"prompt":"Hello world"}' ollama:11434/api/generate | jq -r .response
    ```

=== "Gitlab CI"

    ```yaml
    before_script: apk add jq
    script: |
      curl -sS -X POST -d '{"model":"llama3.2","stream":false}' ollama:11434/api/pull | jq -r .status
      curl -sS -X POST -d '{"model":"llama3.2","stream":false,"prompt":"Hello world"}' ollama:11434/api/generate | jq -r .response
    ```

This looks much better:

```
> curl -sS -X POST -d '{"model":"llama3.2","stream":false}' ollama:11434/api/pull | jq -r .status
success
> curl -sS -X POST -d '{"model":"llama3.2","stream":false,"prompt":"Hello world"}' ollama:11434/api/generate | jq -r .response
Hello! It's nice to meet you. Is there something I can help you with or would you like to chat?
```

### Put it all together

This is our final product:

=== "GitHub Actions - `.github/workflows/ci.yml`"

    ```yaml
    name: ci
    on:
      push:

    jobs:
      ollama:
        runs-on: ubuntu-latest
        services:
          ollama: ollama/ollama
        container: alpine/curl
        steps:
          - name: Install jq
            run: apk add jq
          - name: Generate response
            run: |
              curl -sS -X POST -d '{"model":"llama3.2","stream":false}' ollama:11434/api/pull | jq -r .status
              curl -sS -X POST -d '{"model":"llama3.2","stream":false,"prompt":"Hello world"}' ollama:11434/api/generate | jq -r .response
    ```

=== "Gitlab CI - `.gitlab-ci.yml`"

    ```yaml
    workflow:
      name: ci

    ollama:
      image: alpine/curl
      services:
        - name: ollama/ollama
          alias: ollama
      before_script: apk add jq
      script: |
        curl -sS -X POST -d '{"model":"llama3.2","stream":false}' ollama:11434/api/pull | jq -r .status
        curl -sS -X POST -d '{"model":"llama3.2","stream":false,"prompt":"Hello world"}' ollama:11434/api/generate | jq -r .response
    ```

## Summary

With just a few lines of code, we're able to run an Ollama server, pull down a large language model, and generate responses--all completely local to our CI job. We can now use this capability to generate release notes, automate code review, write documentation--the possibilities are endless.

[^1]: [Creating a GitHub repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories)
[^2]: [Creating a Gitlab project](https://docs.gitlab.com/ee/user/project/)
[^3]: [GitHub actions - `services`](https://docs.github.com/en/actions/use-cases-and-examples/using-containerized-services/about-service-containers)
[^4]: [Gitlab CI - `services`](https://docs.gitlab.com/ee/ci/services/)
