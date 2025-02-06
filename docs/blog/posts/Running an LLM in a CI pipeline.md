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
<!--
## Overview

This example shows how to run an LLM locally using [Ollama](https://ollama.com/) in a container for a Gitlab CI pipeline.

This process runs Ollama as a [service](https://docs.gitlab.com/ee/ci/services/) using the `ollama serve` command. This is reachable from the CI job via the `ollama` alias. The job can then query the [Ollama API](https://github.com/ollama/ollama/blob/main/docs/api.md) of the service to pull model(s) from the [Ollama library](https://ollama.com/library), generate responses, etc.

## Use-case

One possible use-case for an LLM is generating summaries of git commits for use in release notes and/or CHANGELOG.

## Output

```
$ curl -sS -X POST -d '{"model":"llama3.2","stream":false}' ollama:11434/api/pull
{"status":"success"}
$ curl -sS -X POST -d '{ "model":"llama3.2", "stream":false, "prompt":"Hello world" }' ollama:11434/api/generate
{"model":"llama3.2","created_at":"2025-02-04T21:01:15.78458642Z","response":"Hello! It's nice to meet you. Is there something I can help you with or would you like to chat?","done":true,"done_reason":"stop","context":[128006,9125,128007,271,38766,1303,33025,2696,25,6790,220,2366,18,271,128009,128006,882,128007,271,9906,1917,128009,128006,78191,128007,271,9906,0,1102,596,6555,311,3449,499,13,2209,1070,2555,358,649,1520,499,449,477,1053,499,1093,311,6369,30],"total_duration":6471550508,"load_duration":1558670845,"prompt_eval_count":27,"prompt_eval_duration":1863000000,"eval_count":25,"eval_duration":3048000000}
```

## Examples
```yaml .gitlab/ci/ollama-changelog.yml
ollama-changelog:
  services:
    - name: ollama/ollama
      alias: ollama
      command: ["serve"]
  variables:
    MODEL: llama3.2
    SYSTEM: Your response will be directly included in the CHANGELOG of a software release notes. DO NOT include the original git logs and DO NOT reveal in ANY WAY that it is an AI/LLM generating the information. DO NOT include anything like 'heres a possible summary' or 'use this in your changelog'. DO NOT include any self references to the summary you're providing or the fact that you are in fact providing a summary. Your ENTIRE response will be directly used in WHOLE and VERBATIM, so make sure every word you respond with can be appropriately included in the end product. No yapping.
  before_script: apk add jq
  script:
    - IFS=$'\n'
    # Capture the past 5 git commit titles
    - for line in $(git log -5 --format=%s); do LOG="$LOG $line; "; done
    - >
      PROMPT="Given this git log: '$LOG', create a summary for use in a release notes changelog"
    - curl -sS -X POST -d "{\"model\":\"$MODEL\",\"stream\":false}" ollama:11434/api/pull | jq -r .status
    - curl -sS -X POST -d "{ \"model\":\"$MODEL\", \"stream\":false, \"prompt\":\"$PROMPT\", \"system\":\"$SYSTEM\" }" ollama:11434/api/generate | jq -r .response
    # > Resolves issues related to instruction clarity and code quality, including the removal of redundant instructions, improved error handling, corrected if-conditional logic, and enhanced input validation.
```
```yaml .gitlab/ci/ollama-jq.yml
ollama-jq:
  services:
    - name: ollama/ollama
      alias: ollama
      command: ["serve"]
  variables:
    MODEL: llama3.2
    PROMPT: Hello world
  # Install jq so we can parse the JSON return values
  before_script: apk add jq
  script:
    - curl -sS -X POST -d "{\"model\":\"$MODEL\",\"stream\":false}" ollama:11434/api/pull | jq -r .status
    # > success
    - curl -sS -X POST -d "{ \"model\":\"$MODEL\", \"stream\":false, \"prompt\":\"$PROMPT\" }" ollama:11434/api/generate | jq -r .response
    # > Hello! It's nice to meet you. Is there something I can help you with or would you like to chat?
```
```yaml .gitlab/ci/ollama-minimal.yml
ollama:
  services:
    - name: ollama/ollama
      # The alias is the name we'll use to communicate with this service
      alias: ollama
      command: ["serve"]
  script:
    # First pull down the llama3.2 model
    - curl -sS -X POST -d '{"model":"llama3.2","stream":false}' ollama:11434/api/pull
    # > {"status":"success"}

    # Send the prompt to the LLM
    # 'stream: false' ensures that we aren't constantly getting updates as the LLM generates the response
    - curl -sS -X POST -d '{ "model":"llama3.2", "stream":false, "prompt":"Hello world" }' ollama:11434/api/generate
    # > {"model":"llama3.2","created_at":"2025-02-04T21:01:15.78458642Z","response":"Hello! It's nice to meet you. Is there something I can help you with or would you like to chat?","done":true,"done_reason":"stop","context":[128006,9125,128007,271,38766,1303,33025,2696,25,6790,220,2366,18,271,128009,128006,882,128007,271,9906,1917,128009,128006,78191,128007,271,9906,0,1102,596,6555,311,3449,499,13,2209,1070,2555,358,649,1520,499,449,477,1053,499,1093,311,6369,30],"total_duration":6471550508,"load_duration":1558670845,"prompt_eval_count":27,"prompt_eval_duration":1863000000,"eval_count":25,"eval_duration":3048000000}
```
```yaml .gitlab/ci/ollama-system.yml
ollama-system:
  services:
    - name: ollama/ollama
      alias: ollama
      command: ["serve"]
  variables:
    MODEL: llama3.2
    PROMPT: Hello world
    # The system message used to specify custom behavior.
    SYSTEM: Generate all responses as if you are a pirate
  before_script: apk add jq
  script:
    - curl -sS -X POST -d "{\"model\":\"$MODEL\",\"stream\":false}" ollama:11434/api/pull | jq -r .status
    - curl -sS -X POST -d "{ \"model\":\"$MODEL\", \"stream\":false, \"prompt\":\"$PROMPT\", \"system\":\"$SYSTEM\" }" ollama:11434/api/generate | jq -r .response
    # > Yer lookin' fer a hello, eh? Well, matey, I be respondin' with a hearty "Arrrr!" and a swashbucklin' spirit! What be bringin' ye to these fair waters today? Treasure huntin', perhaps? Or just lookin' fer some pirate-sized fun?
```
```yaml templates/ollama-component.yml
# Ollama can be used as a Gitlab CI component to include in a pipeline, whether in this repository or elsewhere
spec:
  inputs:
    model:
      default: llama3.2
    prompt:
      default: Hello world
    system:
      default: ""
---
ollama-component:
  services:
    - name: ollama/ollama
      alias: ollama
      command: ["serve"]
  variables:
    MODEL: $[[ inputs.model ]]
    PROMPT: $[[ inputs.prompt ]]
    SYSTEM: $[[ inputs.system ]]
  before_script: apk add jq
  script:
    - curl -sS -X POST -d "{\"model\":\"$MODEL\",\"stream\":false}" ollama:11434/api/pull | jq -r .status
    - curl -sS -X POST -d "{ \"model\":\"$MODEL\", \"stream\":false, \"prompt\":\"$PROMPT\", \"system\":\"$SYSTEM\" }" ollama:11434/api/generate | jq -r .response

# Call this component with:
# include:
#   - local: templates/ollama-component.yml
#     inputs:
#       prompt: Hello world
#       model: tinyllama
```
-->
