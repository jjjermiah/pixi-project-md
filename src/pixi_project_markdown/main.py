from rich import print as rprint


def hello() -> tuple[str, str]:
    """Return a greeting message and an emoji."""
    return "Hello from pixi_project_markdown, [bold magenta]World[/bold magenta]!", ":vampire:"


def main() -> None:
    """Print a greeting message and an emoji."""
    rprint(*hello())

if __name__ == "__main__":
  main()
