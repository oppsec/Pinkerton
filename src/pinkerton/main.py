from requests import get, exceptions
from urllib3 import disable_warnings
from rich import print
import re

disable_warnings()

def check_host(args) -> None:
    " Check if hosts is alive "

    try:
        response = get(args.u, verify=False)
        status_code: int = response.status_code
        body: str = response.text

        status_error = f"[bold white on red][!] Host returned status code {status_code} [/]"

        alive = lambda success = 200: status_code == success
        (extract_js(args, body)) if alive() else print(status_error)

    except exceptions.ConnectionError as con_error:
        return print(f"[red][!] Connection error on host {args.u} | {con_error} [/]")
    except exceptions.InvalidURL as invalid_error:
        return print(f"[red][!] You've passed an invalid url | {invalid_error} [/]")

def extract_js(args, body):
    " Extract JavaScript files links from page source "

    print(f"[bold on green] Extracting JavaScript files from [white]{args.u}[/] [/]")
    
    #pattern = r'/src="(.+\.js)"/g'
    pattern = r'src="(.*\.js)"'
    link = re.findall(pattern, body)

    print(link)