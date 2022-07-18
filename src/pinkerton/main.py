import re

from requests import get, exceptions
from urllib3 import disable_warnings
from rich import print

from src.pinkerton.settings import props
from src.pinkerton.modules.secret import direct_scan, passed_scan

disable_warnings()

def check_host(args) -> None:
    " Check if hosts is alive "

    url = args.u

    try:
        response = get(url, **props)
        status_code: int = response.status_code
        body: str = response.text

        status_error: str = f"[bold white on red][!] Host returned status code: {status_code} [/]"

        if response.ok:
            print(f"[bold white on green]> Connected sucessfully with [bold white on yellow]{url}[/][/]")
            extract_js(url, body)
        else:
            return print(status_error)

    except exceptions.ConnectionError as con_error:
        return print(f"[red][!] Connection error on host {args.u} | {con_error} [/]")
    except exceptions.InvalidURL as invalid_error:
        return print(f"[red][!] You've passed an invalid url | {invalid_error} [/]")


def extract_js(url, body) -> None:
    " Extract JavaScript files links from page source "

    # Connected sucessfully with target and start extractor
    print(f"\n[bold white on green][*] Extracting JavaScript files from [white on yellow]{url}[/][/]")

    re_jsfiles = r'src="(.*?\.js)"'
    jsfiles_urls = re.findall(re_jsfiles, body)

    # Return number of JavaScript files found on the webpage source
    print(f"[bold white on green][*] Scanning {len(jsfiles_urls)} JavaScript files [/]")

    for urls in jsfiles_urls:
        final_url = f"{url}{urls}"

        if urls.startswith("http"):
            print(f"[bold white on green] > Scanning: [bold white on yellow]{urls}[/][/]")
            direct_scan(urls)
        else:
            print(f"[bold white on green] > Scanning: [bold white on yellow]{final_url}[/][/]")
            passed_scan(final_url)
