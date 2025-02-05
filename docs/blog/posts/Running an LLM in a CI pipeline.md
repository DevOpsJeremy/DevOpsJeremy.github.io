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
| Ollama | A free, open-source tool for running LLMs locally |
| Gitlab CI | A free CI/CD pipeline system developed by Gitlab for running automated jobs in the same environment as your git repository |
| Github Actions | Same as Gitlab CI, but provided by Github |

!!! note

    In this article I won't be getting too deep into exactly what Ollama is and how it works. To learn more about it, check out their [GitHub](https://github.com/ollama/ollama).

### Setup

To start, you'll need either a [Github](https://github.com) or [Gitlab](https://gitlab.com) account and you'll need to create your first repository[^1][^2]. Once that's done, create a basic CI/CD pipeline:

=== "Github Actions - `.github/workflows/ci.yml`"

    ```yaml
    name: ci
    on:
      push:
        branches:
          - main
    ```

=== "Gitlab CI - `.gitlab-ci.yml`"

    ```yaml
    workflow:
      name: ci
      rules:
        - if: $CI_COMMIT_BRANCH == 'main'
    ```

This creates a basic structure for a pipeline that runs on the `main` branch. Feel free to use whichever branch you want, or omit it entirely to run on all branches.

### Running an LLM in a job

The `ollama` CLI is great for when you want to run a local, interactive chat session in your terminal. But for a non-interactive, automated CI job it's best to interface with the [Ollama API](https://github.com/ollama/ollama/blob/main/docs/api.md). To do this, we need to first run Ollama as a service[^3][^4] accessible by our job.

=== "Github Actions"

    ```yaml
    jobs:
      ollama:
        runs-on: ubuntu-latest
        services:
          ollama:
            image: ollama/ollama
            options: serve
    ```

=== "Gitlab CI"

    ```yaml
    ollama:
      services:
        - image: ollama/ollama
          alias: ollama
          command: ["serve"]
    ```

[^1]: [Creating a GitHub repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories)
[^2]: [Creating a Gitlab project](https://docs.gitlab.com/ee/user/project/)
[^3]: [GitHub actions - services](https://docs.github.com/en/actions/use-cases-and-examples/using-containerized-services/about-service-containers)
[^4]: [Gitlab CI - services](https://docs.gitlab.com/ee/ci/services/)
