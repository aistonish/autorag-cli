import platform
import subprocess  # noqa: S404
from pathlib import Path

import cpuinfo
import GPUtil
import psutil
import srsly

from autorag.init.system_specs import (
    CPUSpecs,
    DiskSpecs,
    GPUSpecs,
    MemorySpecs,
    OSSpecs,
    SystemSpecs,
)
from autorag.logging import logger


def __get_os_specs() -> OSSpecs:
    docker_version_info = subprocess.run(
        ["docker", "version", "-f", "json"],  # noqa: S603, S607
        capture_output=True,
        check=False,
    )
    docker_available = docker_version_info.returncode == 0
    docker_version = "N/A"
    if docker_available:
        version_info_dict = srsly.json_loads(docker_version_info.stdout)
        docker_version = version_info_dict["Client"]["Version"]

    os_specs = OSSpecs(
        os=platform.system(),
        os_version=platform.version(),
        docker=docker_available,
        docker_version=docker_version,
    )

    return os_specs


def __get_cpu_specs() -> CPUSpecs:
    cpu_specs = CPUSpecs(
        model=cpuinfo.get_cpu_info()["brand_raw"],
        brand=cpuinfo.get_cpu_info()["arch_string_raw"],
        cores=psutil.cpu_count(logical=False),
        threads=psutil.cpu_count(logical=True),
    )

    return cpu_specs


def __get_memory_specs() -> MemorySpecs:
    memory = psutil.virtual_memory()
    memory_specs = MemorySpecs(
        total=memory.total,
        available=memory.available,
        used=memory.used,
        free=memory.free,
    )

    return memory_specs


def __get_disk_specs() -> DiskSpecs:
    disk = psutil.disk_usage("/")
    disk_specs = DiskSpecs(
        total=disk.total,
        used=disk.used,
        free=disk.free,
    )

    return disk_specs


def __get_gpu_specs() -> list[GPUSpecs]:
    gpu_specs = []
    gpus = GPUtil.getGPUs()
    if gpus:
        for gpu in gpus:
            gpu_specs.append(
                GPUSpecs(
                    name=gpu.name,
                    memory_total=gpu.memoryTotal,
                    memory_used=gpu.memoryUsed,
                    memory_free=gpu.memoryFree,
                    temperature=gpu.temperature,
                    load=gpu.load,
                )
            )
    return gpu_specs


def _get_system_specs() -> SystemSpecs:
    os_specs = __get_os_specs()
    cpu_specs = __get_cpu_specs()
    memory_specs = __get_memory_specs()
    disk_specs = __get_disk_specs()
    gpu_specs = __get_gpu_specs()

    return SystemSpecs(
        os=os_specs,
        cpu=cpu_specs,
        memory=memory_specs,
        disk=disk_specs,
        gpus=gpu_specs,
    )


def _write_system_specs(specs: SystemSpecs, specs_file: Path) -> None:
    logger.info(f"{specs}")
    srsly.write_yaml(specs_file, specs.dict())
    logger.info(f"Wrote specs to {specs_file}")


def read_system_specs(specs_file: Path) -> SystemSpecs:
    if not specs_file.exists():
        msg = (
            f"System specs file not found at {specs_file}!"
            " Run `autorag init` first or specify the correct spacs file path!"
        )
        logger.error(msg)
        raise FileNotFoundError(msg)
    try:
        specs = srsly.read_yaml(specs_file)
    except Exception as e:
        logger.error(f"Error reading system specs from {specs_file}: {e}")
        raise
    try:
        specs = SystemSpecs(**specs)
    except Exception as e:
        logger.error(f"Error parsing system specs from {specs_file}: {e}")
        raise
    return specs


def print_system_specs(specs_file: Path) -> None:
    specs = read_system_specs(specs_file)
    logger.info(f"System specs at {specs_file}:{specs}")


def generate_system_specs(
    *,
    specs_file: Path,
    force: bool = False,
) -> None:
    logger.info("Starting AutoRAG initialization!")

    if specs_file.exists() and not force:
        msg = f"System specs file already exists at {specs_file}! " "To overwrite it, run `autorag init --force`"
        print_system_specs(specs_file)
        logger.error(msg)
        raise SystemExit(msg)

    elif specs_file.exists() and force:
        logger.warn(f"Overwriting existing system specs file {specs_file}")
        specs_file.unlink()
    else:
        specs_file.parent.mkdir(parents=True, exist_ok=True)

    specs = _get_system_specs()
    _write_system_specs(specs, specs_file)

    logger.info("AutoRAG initialization complete!")
