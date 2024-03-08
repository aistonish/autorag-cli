from pathlib import Path

from autorag.init.generate_system_specs import read_system_specs
from autorag.logging import logger


def configure_system(specs_file: Path) -> None:
    """
    :mag: Configure the AutoRAG :dizzy: system based on the generated specs file.
    """
    logger.info(f"Configuring the AutoRAG system based on the specs file: {specs_file}")
    try:
        _ = read_system_specs(specs_file)
    except FileNotFoundError as e:
        msg = f"Specs file not found: {specs_file}. Please run `autorag init` to generate the specs file."
        logger.error(msg)
        raise SystemExit(msg) from e

    logger.info("This is not yet implemented. Please check back later.")
