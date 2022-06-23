# In development

from requests import get
from rich import print
from src.pinkerton.settings import props

import re

regex_list = {
    'google_api': r'AIza[0-9A-Za-z-_]{35}',
    'firebase': r'AAAA[A-Za-z0-9_-]{7}:[A-Za-z0-9_-]{140}',
    'google_captcha': r'6L[0-9A-Za-z-_]{38}|^6[0-9a-zA-Z_-]{39}$',
    'amazon_aws_access_key_id': r'A[SK]IA[0-9A-Z]{16}',
    'amazon_aws_auth_token': r'amzn\\.mws\\.[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}',
    'authorization_bearer': r'bearer [a-zA-Z0-9_\-\.=:_\+\/]{5,100}',
    'authorization_basic': r'basic [a-zA-Z0-9=:_\+\/-]{5,100}',
    'authorization_api' : r'api[key|_key|\s+]+[a-zA-Z0-9_\-]{5,100}',
    'paypal_braintree_access_token' : r'access_token\$production\$[0-9a-z]{16}\$[0-9a-f]{32}',
    'mailgun_api_key' : r'key-[0-9a-zA-Z]{32}',
    'rsa_private_key' : r'-----BEGIN RSA PRIVATE KEY-----',
    'json_web_token' : r'ey[A-Za-z0-9-_=]+\.[A-Za-z0-9-_=]+\.?[A-Za-z0-9-_.+/=]*$',
    'facebook_access_token' : r'EAACEdEose0cBA[0-9A-Za-z]+',
    'amazon_aws_url' : r's3\.amazonaws.com[/]+|[a-zA-Z0-9_-]*\.s3\.amazonaws.com',
    'google_oauth'   : r'ya29\.[0-9A-Za-z\-_]+',
    'github_access_token' : r'[a-zA-Z0-9_-]*:[a-zA-Z0-9_\-]+@github\.com*',
    'slack_token' : r"\"api_token\":\"(xox[a-zA-Z]-[a-zA-Z0-9-]+)\"",
}

def return_regex_list() -> None:
    " Extract each regex pattern from regex_list list "

    for pattern_name, pattern_value in regex_list.items():
        return(pattern_name, pattern_value)

def direct_scan(link) -> None:
    " Open JavaScript file without parsing URL before requesting "
    
    response: function = get(link, **props)
    content: str = response.text

    for key, value in regex_list.items():
        pattern = value
        match = re.findall(pattern, content)

        if(match):
            print(f"\n[bold white on black][!] {key} found in {link}: {match} [/]\n")
        else:
            pass

def passed_scan(final_url):
    " Parse the URL before open JavaScript directly "

    response: function = get(final_url, **props)
    content: str = response.text

    for key, value in regex_list.items():
        pattern = value
        match = re.findall(pattern, content)

        if(match):
            print(f"\n[bold white on black][!] {key} found in {final_url}: {match} [/]\n")
        else:
            pass