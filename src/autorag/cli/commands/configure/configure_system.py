import sys
from pathlib import Path

from streamlit.web import cli as stcli

from autorag.cli.commands.init.generate_system_specs import read_system_specs
from autorag.cli.commands.init.system_specs import SystemSpecs
from autorag.cli.logging import logger


def _start_streamlit_configurator_ui():
    # https://stackoverflow.com/questions/62760929/how-can-i-run-a-streamlit-app-from-within-a-python-script
    sys.argv = [
        "streamlit",
        "run",
        f"{Path(__file__).parent}/ui/app.py",
        "--client.showSidebarNavigation",
        "false",
    ]
    stcli.main()


def configure_system(specs_file: Path) -> None:
    """
    :rocket: Configure the AutoRAG :dizzy: system based on the generated specs file.
    """
    logger.info(f"Configuring the AutoRAG system based on the specs file: {specs_file}")
    try:
        specs: SystemSpecs = read_system_specs(specs_file)
    except FileNotFoundError as e:
        msg = f"Specs file not found: {specs_file}. Please run `autorag init` to generate the specs file."
        logger.error(msg)
        raise SystemExit(msg) from e

    if not specs.os.docker:
        msg = "Docker was not found on the system. Please install Docker to continue."
        logger.error(msg)
        raise SystemExit(msg)

    _start_streamlit_configurator_ui()

    logger.info("This is not yet implemented. Please check back later.")
