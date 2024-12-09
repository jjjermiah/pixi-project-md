from enum import Enum
from typing import List, Optional
from dataclasses import dataclass

class Platform(Enum):
    LINUX_64 = "linux-64"
    OSX_64 = "osx-64"
    OSX_ARM64 = "osx-arm64"
    WIN_64 = "win-64"


@dataclass
class EnvironmentsInfo:
    name: str
    features: List[str]
    solve_group: Optional[str]
    environment_size: None
    dependencies: List[str]
    pypi_dependencies: List[str]
    platforms: List[Platform]
    tasks: List[str]
    channels: List[str]
    prefix: str


@dataclass
class GlobalInfo:
    bin_dir: str
    env_dir: str
    manifest: str


@dataclass
class ProjectInfo:
    name: str
    manifest_path: str
    last_updated: str
    pixi_folder_size: None
    version: None


@dataclass
class Pixi:
    platform: Platform
    virtual_packages: List[str]
    version: str
    cache_dir: str
    cache_size: None
    auth_dir: str
    global_info: GlobalInfo
    project_info: ProjectInfo
    environments_info: List[EnvironmentsInfo]
    config_locations: List[str]