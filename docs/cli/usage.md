# AutoRAG :dizzy: CLI Admin Guide

## :bulb: Overview
AutoRAG CLI is a command-line interface for AutoRAG, a solution that automates the setup of Retrieval Augmented Generation (RAG) systems. AutoRAG empowers companies with limited AI experience, modest compute resources, and strict data privacy restrictions to easily implement an LLM-powered chatbot that leverages their private data, enhancing customer support, knowledge base access, and more.

This guide provides an overview of the AutoRAG CLI and its usage for system administrators.

## :rocket: Getting Started

1. **Prerequisites:**
    - Linux or macOS
    - Python 3.10 or higher
2. **Installation:**
    - `pip install autorag-cli`

## :gear: AutoRAG Setup
The AutoRAG setup works in three easy steps:

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
