---
title: The changes matrix
summary: Running a job for multiple paths
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

I have a repository with a number of Docker image definitions. In my case, these images each have their own context directory. My repository structure looks something like this:

```text
/
|__ src/
    |
    |__ image1/
    |   |__ Dockerfile
    |
    |__ image2/
    |   |__ Dockerfile
    |   |__ package.json
    |
    |__ image3/
        |__ Dockerfile
        |__ requirements.txt
```

I want to run a Docker build whenever each respective image is changed, and then push that image to my registry. But of course, it wouldn't make sense to build and publish all 3 images every time **_one_** of them is modified. When I make a change to `image1`, I _only_ want `image1` to be built and published. And the same for the other images.

I suppose I could have a separate job for each image:

```yaml
image1-build:
  image: docker:cli
  script:
    - docker build -t gitlab.org/my-user/my-repo/image1 src/image1/
    - docker push gitlab.org/my-user/my-repo/image1
  rules:
    - changes:
        - src/image1/**/*

image2-build:
  image: docker:cli
  script:
    - docker build -t gitlab.org/my-user/my-repo/image2 src/image2/
    - docker push gitlab.org/my-user/my-repo/image2
  rules:
    - changes:
        - src/image2/**/*

image3-build:
  image: docker:cli
  script:
    - docker build -t gitlab.org/my-user/my-repo/image3 src/image3/
    - docker push gitlab.org/my-user/my-repo/image3
  rules:
    - changes:
        - src/image3/**/*
```

As you can see, this is cumbersome, not very scalable, and results in quite a bit of duplicated code.

## The solution

We can solve this with clever use of the [`matrix`](https://docs.gitlab.com/ci/yaml/#parallelmatrix) configuration. But first, you'll need to understand what matrix is used for.

### What is matrix?

Typically `matrix` is used to run multiple jobs in parallel with varying values. See this example from Gitlab's documentation:

```yaml
matrix test:
  parallel:
    matrix:
      - VALUE: [value1, value2, value3]
  script: "echo Test value: $VALUE"
```

This creates 3 separate jobs, outputting the respective value:

> Test value: value1

> Test value: value2

> Test value: value3

### How does this help us?

With `parallel:matrix` we can create individual jobs for each of our Docker contexts:

```yaml
docker:
  image: docker:cli
  variables:
    CONTEXT_ROOT: src
    CONTEXT: $CONTEXT_ROOT/$IMAGE
  parallel:
    matrix:
      - IMAGE:
          - image1
          - image2
          - image3
  script:
    - docker build -t gitlab.org/my-user/my-repo/image3 src/image3/
    - docker push gitlab.org/my-user/my-repo/image3
  rules:
    - changes:
        - Dockerfile
```
