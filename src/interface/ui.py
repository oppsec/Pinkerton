from rich import print

def banner() -> str:
    " Return the content from banner.txt file as application banner "

    path: str = "src/interface/banner.txt"
    with open(path) as file:
        lines: str = file.read()
        print(f"[bold yellow]{lines}[/]")