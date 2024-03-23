import srsly
from pydantic import BaseModel, Field


class CPUSpecs(BaseModel):
    model: str = Field(description="CPU model", default="N/A")
    brand: str = Field(description="CPU brand", default="N/A")
    cores: int = Field(description="Number of CPU cores", default=0)
    threads: int = Field(description="Number of CPU threads", default=0)


class MemorySpecs(BaseModel):
    total: int = Field(description="Total memory in bytes", default=0)
    available: int = Field(description="Available memory in bytes", default=0)
    used: int = Field(description="Used memory in bytes", default=0)
    free: int = Field(description="Free memory in bytes", default=0)


class DiskSpecs(BaseModel):
    total: int = Field(description="Total disk space in bytes", default=0)
    used: int = Field(description="Used disk space in bytes", default=0)
    free: int = Field(description="Free disk space in bytes", default=0)


class GPUSpecs(BaseModel):
    name: str = Field(description="GPU name", default="N/A")
    memory_total: int = Field(description="Total memory in bytes", default=0)
    memory_used: int = Field(description="Used memory in bytes", default=0)
    memory_free: int = Field(description="Free memory in bytes", default=0)
    temperature: float = Field(description="Temperature in Celsius", default=0.0)
    load: float = Field(description="GPU load in percentage", default=0.0)


class OSSpecs(BaseModel):
    os: str = Field(description="OS", default="N/A")
    os_version: str = Field(description="OS version", default="N/A")
    docker: bool = Field(
        description="Whether docker is installed",
        default=False,
    )
    docker_version: str = Field(description="Docker version if docker is installed", default="N/A")


class SystemSpecs(BaseModel):
    os: OSSpecs = Field(description="OS specs", default_factory=OSSpecs)
    cpu: CPUSpecs = Field(description="CPU specs", default_factory=CPUSpecs)
    memory: MemorySpecs = Field(
        description="Memory space",
        default_factory=MemorySpecs,
    )
    disk: DiskSpecs = Field(
        description="Disk space",
        default_factory=DiskSpecs,
    )
    gpus: list[GPUSpecs] = Field(
        description="List of GPUs",
        default_factory=list,
    )

    def __str__(self) -> str:
        return f"\n\n{srsly.yaml_dumps(self.dict())}\n"

    def __repr__(self) -> str:
        return self.__str__()
