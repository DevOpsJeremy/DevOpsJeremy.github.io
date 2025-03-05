---
title: Using `glab` in a CI pipeline with Gitlab self-hosted
date:
  created: 2025-03-04
authors:
  - jeremy
tags:
  - gitlab
  - gitlab ci
  - ci/cd
---
# Using `glab` in a CI pipeline with Gitlab self-hosted

## Overview

The [`glab`](https://docs.gitlab.com/editor_extensions/gitlab_cli/) tool is Gitlab's new (ish) command-line tool for interfacing with the Gitlab API. This article describes how to use `glab` in a Gitlab CI/CD pipeline--particularly if using a self-hosted Gitlab instance.

## Running `glab`

### Configuration

Configurations for the `glab` CLI can be stored in `~/.gitlab/glab-cli/config.yml`, or an alternate directory defined by `$GLAB_CONFIG_DIR`[^1]. Alternatively, many of these configurations can be set as environment variables[^2]. The main configurations we'll need to set for a self-hosted Gitlab instance are:

| Configuration | Variable | Description |
| --- | --- | --- |
| `hosts.<hostname>.api_host` | `GITLAB_API_HOST` | Specify the host where the API endpoint is found. Useful when there are separate (sub)domains or hosts for Git and the API endpoint. |
| `host` | `GITLAB_HOST` | Alias of GITLAB_URI. |
| | `GITLAB_REPO` | Default GitLab repository used for commands accepting the --repo option. Only used if no --repo option is given. |
| `hosts.<hostname>.token` | `GITLAB_TOKEN` | an authentication token for API requests. Setting this avoids being prompted to authenticate and overrides any previously stored credentials. Can be set in the config with glab config set token xxxxxx. |
| | `GITLAB_URI` | Alias of GITLAB_HOST. |

[^1]: [`glab` config](https://gitlab.com/gitlab-org/cli/-/blob/main/README.md#configuration)
[^2]: [`glab` environment variables](https://gitlab.com/gitlab-org/cli/-/blob/main/README.md#environment-variables)
