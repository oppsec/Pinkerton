import re

from requests import get, exceptions
from urllib3 import disable_warnings
from rich import print

from src.pinkerton.settings import props
from src.pinkerton.modules.secret import direct_scan, passed_scan

disable_warnings()

def perform_checks(args) -> None:
    " Check if hosts is alive "

    global url
    url = args.u

    try:
        response = get(url, **props)
        status_code: int = response.status_code
        page_content: str = response.text

        status_error: str = f"[bold white on red][!] Host returned status code: {status_code}[/]"

        if response.ok:
            print(f"[bold white on green][+] Connected sucessfully with [bold white on yellow]{url}[/][/]")
            extract_js(url, page_content)
        else:
            print(status_error)
            return False

    except exceptions.ConnectionError as con_error:
        print(f"[red][!] Connection error on host {args.u} | {con_error} [/]")
        return False
    except exceptions.InvalidURL as invalid_error:
        print(f"[red][!] You've passed an invalid url | {invalid_error} [/]")
        return False


def extract_js(url, page_content) -> None:
    " Extract JavaScript files links from page source "

    # Connected sucessfully with target and start extractor
    print(f"[bold white on yellow][*] Extracting JavaScript files from {url}")

    js_file_pattern = r'src="(.*?\.js)(\?.*?)?"'
    js_files = re.findall(js_file_pattern, page_content)

    # Return number of JavaScript files found on the webpage source
    print(f"[bold white on green][+] Found [bold white on yellow]{len(js_files)}[/] JavaScript file(s) [/]")

    for jsfile, _ in js_files:
        final_url = f"{url}{jsfile}"

        if jsfile.startswith("http"):
            print(f"[bold white on green][+] Scanning: [bold black on white]{jsfile}[/][/]")
            direct_scan(jsfile)
        else:
            print(f"[bold white on green][+] Scanning: [bold black on white]{final_url}[/][/]")
            passed_scan(final_url)