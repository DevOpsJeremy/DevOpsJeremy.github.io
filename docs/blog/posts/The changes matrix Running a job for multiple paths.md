---
title: 'The changes matrix: Running a job for multiple paths'
date:
  created: 2026-01-26
authors:
  - jeremy
tags:
  - gitlab
  - gitlab ci
  - ci/cd
---

## Overview

One of my most used Gitlab CI feature is the [`changes`](https://docs.gitlab.com/ci/yaml/#ruleschanges) rule. This allows you to run a job or group of jobs based on the changed paths.

Here's a simple example of how `rules:changes` can be used in a pipeline:

```yaml
# Run mkdocs when anything under the docs/ directory is changed
docs:
  image: squidfunk/mkdocs-material
  script: mkdocs build
  rules:
    - changes:
        - docs/**/*

# Run pytest when anything under the src/ directory is changed
tests:
  image: python
  before_script: pip install pytest
  script: pytest
  rules:
    - changes:
        - src/**/*

# Build the Docker image when the Dockerfile is changed
docker:
  image: docker:cli
  script: docker build
  rules:
    - changes:
        - Dockerfile
```

I recently discovered a neat trick for conditionally running the same job based on changes in multiple paths.

## The problem

I have a repository with a number of Docker image definitions
