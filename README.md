# vaulted-zodiac

<!-- ![Build Status](https://img.shields.io/github/actions/workflow/status/shoot649854/vaulted-zodiac/ci.yml?branch=main)
![License](https://img.shields.io/github/license/shoot649854/vaulted-zodiac)
![Version](https://img.shields.io/github/package-json/v/shoot649854/vaulted-zodiac?private=true)
![Dependencies](https://img.shields.io/librariesio/github/shoot649854/vaulted-zodiac?private=true)
![Dev Dependencies](https://img.shields.io/librariesio/github/shoot649854/vaulted-zodiac?private=true&type=dev)
![Issues](https://img.shields.io/github/issues/shoot649854/vaulted-zodiac) -->

![Python](https://img.shields.io/badge/-Python-F9DC3E.svg?logo=python&style=flat)
![TypeScript](https://img.shields.io/badge/-TypeScript-007ACC.svg?logo=typescript&style=flat)
![Flask](https://img.shields.io/badge/-Flask-000000.svg?logo=flask&style=flat)
![React](https://img.shields.io/badge/React-18.3.3-blue)
![Node](https://img.shields.io/badge/Node-20.14.10-green)
![Python Version](https://img.shields.io/badge/python-3.11-blue)

## Description

Vaulted Zodiac is a Flask-based application designed to demonstrate the integration of Flask with SQLAlchemy and PostgreSQL. This project uses Poetry for dependency management and Docker for containerization.

## Prerequisites

-   Python 3.11
-   Docker
-   Docker Compose
-   Homebrew (for installing Graphviz)

## Dependencies

| Package                          | Version |
| -------------------------------- | ------- |
| python                           | ^3.11   |
| flask                            | ^3.0.3  |
| flask-migrate                    | ^4.0.7  |
| sqlalchemy-data-model-visualizer | ^0.1.3  |

## Steps

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/vaulted-zodiac.git
    cd vaulted-zodiac
    ```

2. **Install Poetry**

    ```bash
    pip install poetry
    poetry install --no-root
    poetry run python app.py
    ```

3. **Running frontend**
    ```bash
    pnpm install
    pnpm run start
    ```

### Using Docker

1. **Build Docker Image**
    ```bash
    docker compose up --build
    docker run -p 5000:5000 vaulted-zodiac
    ```

## Deployment

### Environment file

PROJECT_ID and REGION is required to have before deploying.

```bash
PROJECT_ID=""
REGION=""
```

1. **Deploy to Google Cloud**
    ```bash
    bash script/deploy/deploy.sh
    ```

## Database Diagram

You can view the database diagram [here](https://dbdiagram.io/d/668204689939893daea9e196).
