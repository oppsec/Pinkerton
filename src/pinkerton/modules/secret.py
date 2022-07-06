# In development

from requests import get
from rich import print
from src.pinkerton.settings import props

import re

regex_list = {
    'Google API': r'AIza[0-9A-Za-z-_]{35}',
    'Firebase Key': r'AAAA[A-Za-z0-9_-]{7}:[A-Za-z0-9_-]{140}',
    "Firebase URL": r".*firebaseio\.com",
    'Google Captcha Key': r'6L[0-9A-Za-z-_]{38}|^6[0-9a-zA-Z_-]{39}$',
    "Amazon AWS Access Key ID": r"AKIA[0-9A-Z]{16}",
    "Amazon MWS Auth Token": r"amzn\\.mws\\.[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}",
    "Amazon AWS API Key": r"AKIA[0-9A-Z]{16}",
    'Amazon AWS URL' : r's3\.amazonaws.com[/]+|[a-zA-Z0-9_-]*\.s3\.amazonaws.com',
    "Generic API Key": r"[a|A][p|P][i|I][_]?[k|K][e|E][y|Y].*['|\"][0-9a-zA-Z]{32,45}['|\"]",
    "Generic Secret": r"[s|S][e|E][c|C][r|R][e|E][t|T].*['|\"][0-9a-zA-Z]{32,45}['|\"]",
    'Authorization Bearer': r'bearer [a-zA-Z0-9_\-\.=:_\+\/]{5,100}',
    'Authorization Basic': r'basic [a-zA-Z0-9=:_\+\/-]{5,100}',
    'Authorization API Key' : r'api[key|_key|\s+]+[a-zA-Z0-9_\-]{5,100}',
    'PayPal Braintree Access Token' : r'access_token\$production\$[0-9a-z]{16}\$[0-9a-f]{32}',
    'Mailgun API Key' : r'key-[0-9a-zA-Z]{32}',
    "MailChimp API Key": r"[0-9a-f]{32}-us[0-9]{1,2}",
    'RSA Private Key' : r'-----BEGIN RSA PRIVATE KEY-----',
    "Heroku API Key": r"[h|H][e|E][r|R][o|O][k|K][u|U].*[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}",
    'JWT Token' : r'ey[A-Za-z0-9-_=]+\.[A-Za-z0-9-_=]+\.?[A-Za-z0-9-_.+/=]*$',
    "Facebook Access Token": r"EAACEdEose0cBA[0-9A-Za-z]+",
    "Facebook OAuth": r"[f|F][a|A][c|C][e|E][b|B][o|O][o|O][k|K].*['|\"][0-9a-f]{32}['|\"]",
    'Google OAuth' : r'ya29\.[0-9A-Za-z\-_]+',
    "Google Cloud Platform API Key": r"AIza[0-9A-Za-z\\-_]{35}",
    "Google Cloud Platform OAuth": r"[0-9]+-[0-9A-Za-z_]{32}\\.apps\\.googleusercontent\\.com",
    "Google Drive API Key": r"AIza[0-9A-Za-z\\-_]{35}",
    "Google Drive OAuth": r"[0-9]+-[0-9A-Za-z_]{32}\\.apps\\.googleusercontent\\.com",
    "Google (GCP) Service-account": r"\"type\": \"service_account\"",
    "Google Gmail API Key": r"AIza[0-9A-Za-z\\-_]{35}",
    "Google Gmail OAuth": r"[0-9]+-[0-9A-Za-z_]{32}\\.apps\\.googleusercontent\\.com",
    "Google OAuth Access Token": r"ya29\\.[0-9A-Za-z\\-_]+",
    "Google YouTube API Key": r"AIza[0-9A-Za-z\\-_]{35}",
    "Google YouTube OAuth": r"[0-9]+-[0-9A-Za-z_]{32}\\.apps\\.googleusercontent\\.com",
    'Github Access Token' : r'[a-zA-Z0-9_-]*:[a-zA-Z0-9_\-]+@github\.com*',
    "GitHub URL": r"[g|G][i|I][t|T][h|H][u|U][b|B].*['|\"][0-9a-zA-Z]{35,40}['|\"]",
    "Slack Token": r"(xox[p|b|o|a]-[0-9]{12}-[0-9]{12}-[0-9]{12}-[a-z0-9]{32})",
    "Slack Webhook": r"https://hooks.slack.com/services/T[a-zA-Z0-9_]{8}/B[a-zA-Z0-9_]{8}/[a-zA-Z0-9_]{24}",
    "Picatic API Key": r"sk_live_[0-9a-z]{32}",
    "Stripe API Key": r"sk_live_[0-9a-zA-Z]{24}",
    "Stripe Restricted API Key": r"rk_live_[0-9a-zA-Z]{24}",
    "Twitter Access Token": r"[t|T][w|W][i|I][t|T][t|T][e|E][r|R].*[1-9][0-9]+-[0-9a-zA-Z]{40}",
    "Twitter OAuth": r"[t|T][w|W][i|I][t|T][t|T][e|E][r|R].*['|\"][0-9a-zA-Z]{35,44}['|\"]",
    "Twilio API Key": r"SK[0-9a-fA-F]{32}",
    "Square Access Token": r"sq0atp-[0-9A-Za-z\\-_]{22}",
    "Square OAuth Secret": r"sq0csp-[0-9A-Za-z\\-_]{43}",
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
            print(f"\n[bold white][!] {key} found in {link}: {match} [/]\n")
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
            print(f"\n[bold white][!] {key} found in {final_url}: {match} [/]\n")
        else:
            pass