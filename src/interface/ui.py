from rich import print

def banner() -> str:
    " Return the content from banner.txt file as application banner "

    path: str = "src/interface/banner.txt"
    with open(path) as file:
        content = file.read()
        print(f"[bold white]{content}[/]")