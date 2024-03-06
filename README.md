# AIstonish AutoRAG

![AIstonish Logo](assets/logo_draft.png "AIstonish")

# GenAI Chatbots for Everybody 🪄

AutoRAG is an innovative solution that automates the setup of Retrieval Augmented Generation (RAG) systems, empowering companies with:

* Limited AI experience
* Modest compute resources
* Strict data privacy restrictions

With AutoRAG, companies can easily implement an LLM-powered chatbot that leverages their private data, enhancing customer support, knowledge base access, and more.

## Key Features 🪄

* **Super Simple Setup:** Intuitive web app guides users through the entire RAG configuration and deployment process, no AI expertise required.
* **Automated RAG Setup:** Streamlined process for configuring and deploying RAG models.
* **Privacy-Focused:** Designed to prioritize data security and adhere to company-specific data regulations.
* **Resource-Efficient:** Optimized for operation on standard hardware, reducing the need for specialized AI infrastructure.
* **Private Data Integration:** Seamless integration with internal knowledge bases and data sources.
* **Conversational AI Interface:** Intuitive chatbot interface for natural language interactions.

## Getting Started ⚡️

1. **Prerequisites:**
   * [List software dependencies]
   * [Mention required resources, if applicable]
2. **Installation:**
   * `pip install autorag` (or provide alternative instructions)
3. **Access the Web App:**
   * [Provide instructions on how to launch the setup web app]
4. **Follow Guided Setup:**
   * The web app will walk you through connecting data sources and setting preferences.
5. **Deployment:**
   * [Guide on chatbot integration or deployment methods]

## Demo 😲

[Link to a demo video or interactive example, if available]

## Developer Guide 👩🏾‍💻👩‍💻🧑🏾‍💻👨🏼‍💻

### Dev Env Setup
To set up [hatch] and [pre-commit] for the first time:

1. install [hatch] globally, e.g. with [pip], i.e. `pip install hatch`,
2. optionally run `hatch config set dirs.env.virtual .direnv` and `hatch config set dirs.env.pip-compile .direnv`
   to let [VS Code] find your virtual environments,
3. make sure `pre-commit` is installed globally, e.g. with `pip install pre-commit`,
4. run `hatch env create` to create the default virtual environment and install the dependencies,
5. run `hatch run test:no-cov` to run the tests.
6. run `hatch run autorag` to run the package in development mode.

### Local Dev Install
1. run `pip install -e .` to install the package locally in development mode.
2. run `autorag` to run the package and see the help message.

### Test PyPi Dev Install
1. run `pip install -i https://test.pypi.org/simple/ autorag-cli --extra-index-url https://pypi.python.org/simple` to install the package from the test PyPi server.
2. run `autorag` to run the package and see the help message.

### Building and Publishing the Package to (test) PyPi
1. test your changes locally! Make sure everything works as expected using `hatch run autorag [COMMAND]`.
2. run `hatch run test:no-cov` to run the tests.
3. run `hatch run docs:build` to build the documentation.
4. commit, push, and tag the changes you want to release. The tag should be in the Python semantic versioning format: [PEP 404](https://peps.python.org/pep-0440/).
5. run `hatch build` to build the package. Make sure to have the correct version reflected in the built package.
6. run `hatch publish -r test` to publish the package to the test PyPi server.
gcm
## Contributing 👩🏾‍💻👩‍💻🧑🏾‍💻👨🏼‍💻

We welcome contributions to AutoRAG! Please refer to our [CONTRIBUTING.md] file for guidelines.

## License ⚖️

AutoRAG is licensed under the [License Name] ([Link to license])

## Contact ✉️

For support or inquiries, please reach out to [contact@aistonish.de](mailto:contact@aistonish.de)

## Acknowledgements 🙏

This package was created with [The Hatchlor] project template and other great open-source projects.

[The Hatchlor]: https://github.com/florianwilhelm/the-hatchlor
[hatch]: https://hatch.pypa.io/
[pre-commit]: https://pre-commit.com/
[VS Code]: https://code.visualstudio.com/docs/python/environments#_where-the-extension-looks-for-environments
[hatch-pip-compile]: https://github.com/juftin/hatch-pip-compile
