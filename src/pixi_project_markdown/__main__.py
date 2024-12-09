import click
import json
from enum import Enum
from typing import List, Optional
from rich import print as rprint
from pixi_project_markdown.models import (
    TaskInfo,
    Task,
    Feature,
    EnvironmentsInfo,
    GlobalInfo,
    ProjectInfo,
    Platform,
    Pixi,
)

@click.command()
@click.argument("input", type=click.File("rb"), nargs=1)
def cli(input):
    """Create a Pixi instance from a JSON file containing pixi environment information.

    \b
    Parse pixi environment from file:a
        cat pixi.json | pixi_project_markdown
    """

    if input is None:
        raise click.ClickException("No input file provided.")

    
    data = json.load(input)
    pixi = Pixi(
        platform=Platform(data["platform"]),
        virtual_packages=data["virtual_packages"],
        version=data["version"],
        cache_dir=data["cache_dir"],
        cache_size=data["cache_size"],
        auth_dir=data["auth_dir"],
        global_info=GlobalInfo(**data["global_info"]),
        project_info=ProjectInfo(**data["project_info"]),
        environments_info=[EnvironmentsInfo(**env) for env in data["environments_info"]],
        config_locations=data["config_locations"]
    )
    rprint(pixi)
    return pixi

if __name__ == "__main__":
    rprint(cli())