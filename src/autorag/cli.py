from pathlib import Path
from typing import Annotated

import typer
from click import Context
from typer.core import TyperGroup

from autorag import __version__
from autorag.configure.configure_system import configure_system
from autorag.init.generate_system_specs import generate_system_specs, print_system_specs
from autorag.logging import LogLevel, setup_logging


# Custom TyperGroup to list commands in the order appear
class OrderCommands(TyperGroup):
    def list_commands(self, ctx: Context):
        """Return list of commands in the order appear."""
        return list(self.commands)  # get commands using self.commands


app = typer.Typer(
    name=f"AutoRAG {__version__}",
    help="AutoRAG: Unleash On-Premise RAG Solutions for Enhanced Business Performance.",
    rich_markup_mode="rich",
    no_args_is_help=True,
    cls=OrderCommands,
)

ExistingSpecFileType = Annotated[
    Path,
    typer.Option(
        help="The location of the system specs file.",
        exists=True,
        file_okay=True,
        readable=True,
        resolve_path=True,
    ),
]

NonExistingSpecFileType = Annotated[
    Path,
    typer.Option(
        help="The location of the system specs file.",
        exists=False,
        resolve_path=True,
    ),
]

__home__ = Path.home()


@app.command("version")
def version() -> None:
    """
    :bookmark: Print the version of AutoRAG:sparkles:
    """
    print(f"AutoRAG Version: {__version__}")  # noqa: T201
    raise SystemExit()


@app.command("init")
def init(
    specs_file: NonExistingSpecFileType = Path(f"{__home__}/.autorag/init/specs.yaml"),
    *,
    force: Annotated[
        bool,
        typer.Option(
            help="If true, it overwrites existing specs file.",
        ),
    ] = False,
    log_level: Annotated[LogLevel, typer.Option(help="Sets the Log Level")] = LogLevel.INFO,
) -> None:
    """
    :rocket: Initialize AutoRAG:sparkles: by generating the system specs file
    """
    print(f"AutoRAG Version: {__version__}")  # noqa: T201
    setup_logging(log_level)
    generate_system_specs(
        specs_file=specs_file,
        force=force,
    )


@app.command("print-specs")
def print_specs(
    specs_file: ExistingSpecFileType = Path(f"{__home__}/.autorag/init/specs.yaml"),
    log_level: Annotated[LogLevel, typer.Option(help="Sets the Log Level")] = LogLevel.INFO,
) -> None:
    """
    :mag: Print the generated system specs file
    """
    print(f"AutoRAG Version: {__version__}")  # noqa: T201
    setup_logging(log_level)
    print_system_specs(specs_file)


@app.command("configure")
def configure(
    specs_file: ExistingSpecFileType = Path(f"{__home__}/.autorag/init/specs.yaml"),
    log_level: Annotated[LogLevel, typer.Option(help="Sets the Log Level")] = LogLevel.INFO,
) -> None:
    """
    :wrench: Configure the AutoRAG system based on the generated specs file.
    """
    print(f"AutoRAG Version: {__version__}")  # noqa: T201
    setup_logging(log_level)
    configure_system(specs_file)


def main() -> None:
    app()


if __name__ == "__main__":
    main()
