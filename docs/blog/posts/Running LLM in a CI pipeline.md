---
title: Running LLMs in a CI pipeline
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
# Running LLMs in a CI pipeline

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

=== "Gitlab CI - `.gitlab-ci.yml`

    ```yaml
    workflow:
      name: ci
      rules:
        - if: $CI_COMMIT_BRANCH == 'main'
    ```

This creates a basic structure for a pipeline that runs on the `main` branch. Feel free to use whichever branch you want, or omit it entirely to run on all branches.

[^1] https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories
[^2] https://docs.gitlab.com/ee/user/project/
