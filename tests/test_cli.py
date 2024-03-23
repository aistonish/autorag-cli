import tempfile
from pathlib import Path

from typer.testing import CliRunner

from autorag.cli.app import app

runner = CliRunner()


def test_autorag_version():
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
    assert "AutoRAG Version: " in result.stdout


def test_autorag_init():
    with tempfile.TemporaryDirectory() as tmpdir:
        specs_file = f"{tmpdir}/specs.yaml"
        result = runner.invoke(app, ["init", "--specs-file", specs_file])
        assert result.exit_code == 0

        assert Path(specs_file).exists() and Path(specs_file).is_file() and Path(specs_file).stat().st_size > 0


def test_autorag_print_specs():
    with tempfile.TemporaryDirectory() as tmpdir:
        specs_file = f"{tmpdir}/specs.yaml"
        result = runner.invoke(app, ["print-specs", "--specs-file", specs_file])
        assert result.exit_code != 0

        result = runner.invoke(app, ["init", "--specs-file", specs_file])
        assert result.exit_code == 0

        result = runner.invoke(app, ["print-specs", "--specs-file", specs_file])
        assert result.exit_code == 0
