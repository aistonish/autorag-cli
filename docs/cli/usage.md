# AutoRAG :dizzy: CLI Admin Guide

# :construction: WORK IN PROGRESS :construction:
This guide as well as `autorag` is a work in progress and might not be fully functional yet.

## :bulb: Overview
AutoRAG CLI is a command-line interface for AutoRAG, a solution that automates the setup of Retrieval Augmented Generation (RAG) systems. AutoRAG empowers companies with limited AI experience, modest compute resources, and strict data privacy restrictions to easily implement an LLM-powered chatbot that leverages their private data, enhancing customer support, knowledge base access, and more.

This guide provides an overview of the AutoRAG CLI and its usage for system administrators.

## :rocket: Getting Started

1. **Prerequisites:**
    - Linux or macOS
    - Python 3.10 or higher
2. **Installation (Demo from test PyPI):**
    - `pip install -i https://test.pypi.org/simple/ autorag-cli --extra-index-url https://pypi.python.org/simple`

## :gear: AutoRAG Setup
The AutoRAG setup works in three easy steps: initialization, configuration, and deployment.

To get help on the AutoRAG CLI, run the following command:
```bash
autorag [--help]
```
or for a specific command:
```bash
autorag <command> --help
```


### Initialize AutoRAG
In this step `autorag` automatically discovers the system specifications where it is being installed and sets up the environment accordingly.

```bash
autorag init
```

### AutoRAG Configuration
In this step, `autorag` will guide you through the configuration of the AutoRAG service.

```bash
autorag configure
```

###  AutoRAG Deployment
In this step, `autorag` will deploy the AutoRAG service.

```bash
autorag run
```
