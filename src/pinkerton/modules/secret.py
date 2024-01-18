# In development

from requests import get
from rich import print
from jsbeautifier import beautify
from re import findall
from src.pinkerton.settings import props

regex_list = {
    'Google API': r'AIza[0-9A-Za-z-_]{35}',
    "Artifactory API Token": r'(?:\s|=|:|"|^)AKC[a-zA-Z0-9]{10,}',
    "Artifactory Password": r'(?:\s|=|:|"|^)AP[\dABCDEF][a-zA-Z0-9]{8,}',
    "Cloudinary Basic Auth": r"cloudinary:\/\/[0-9]{15}:[0-9A-Za-z]+@[a-z]+",
    'Firebase Key': r'AAAA[A-Za-z0-9_-]{7}:[A-Za-z0-9_-]{140}',
    "LinkedIn Secret Key": r"(?i)linkedin(.{0,20})?['\"][0-9a-z]{16}['\"]",
    "Mailto String": r"(?<=mailto:)[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.-]+",
    "Picatic API Key": r"sk_live_[0-9a-z]{32}",
    "Firebase URL": r".*firebaseio\.com",
    "PGP Private Key Block": r"-----BEGIN PGP PRIVATE KEY BLOCK-----",
    "SSH (DSA) Private Key": r"-----BEGIN DSA PRIVATE KEY-----",
    "SSH (EC) Private Key": r"-----BEGIN EC PRIVATE KEY-----",
    "SSH (RSA) Private Key": r"-----BEGIN OPENSSH PRIVATE KEY-----",
    "SSH (ssh-ed25519) Public Key": r"ssh-ed25519",
    'Google Captcha Key': r'6L[0-9A-Za-z-_]{38}|^6[0-9a-zA-Z_-]{39}$',
    "Amazon AWS Access Key ID": r"AKIA[0-9A-Z]{16}",
    "Amazon MWS Auth Token": r"amzn\\.mws\\.[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}",
    "Amazon AWS API Key": r"AKIA[0-9A-Z]{16}",
    'Amazon AWS URL' : r's3\.amazonaws.com[/]+|[a-zA-Z0-9_-]*\.s3\.amazonaws.com',
    "Generic API Key": r"(?i)api[_]?key.*['|\"]\w{32,45}['|\"]",
    "Generic Secret": r"(?i)secret.*['|\"]\w{32,45}['|\"]",
    'Authorization Bearer': r'bbearer [a-zA-Z0-9_\\-\\.=]+',
    'Authorization Basic': r'basic [a-zA-Z0-9=:_\+\/-]{5,100}',
    'Authorization API Key' : r'api[key|_key|\s+]+[a-zA-Z0-9_\-]{5,100}',
    'PayPal Braintree Access Token' : r'access_token\$production\$[0-9a-z]{16}\$[0-9a-f]{32}',
    'Mailgun API Key' : r'key-[0-9a-zA-Z]{32}',
    "MailChimp API Key": r"[0-9a-f]{32}-us[0-9]{1,2}",
    'RSA Private Key' : r'-----BEGIN RSA PRIVATE KEY-----',
    "Heroku API Key": r"(?i)heroku.*[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}",
    "JWT Token": r'ey[A-Za-z0-9-_=]+\.[A-Za-z0-9-_=]+\.?[A-Za-z0-9-_.+/=]*$',
    "Facebook Access Token": r"EAACEdEose0cBA[0-9A-Za-z]+",
    "Facebook OAuth": r"(?i)facebook.*['|\"][0-9a-f]{32}['|\"]",
    "Google OAuth" : r'ya29\.[0-9A-Za-z\-_]+',
    "Facebook Client ID": r"""(?i)(facebook|fb)(.{0,20})?['\"][0-9]{13,17}""",
    "Google Cloud Platform API Key": r"(?i)\b(AIza[0-9A-Za-z\\-_]{35})(?:['|\"|\n|\r|\s|\x60]|$)",
    "Google Cloud Platform OAuth": r"[0-9]+-[0-9A-Za-z_]{32}\\.apps\\.googleusercontent\\.com",
    "Google Drive API Key": r"AIza[0-9A-Za-z\\-_]{35}",
    "Google Drive OAuth": r"[0-9]+-[0-9A-Za-z_]{32}\\.apps\\.googleusercontent\\.com",
    "Google (GCP) Service-account": r"\"type\": \"service_account\"",
    "Google Gmail API Key": r"AIza[0-9A-Za-z\\-_]{35}",
    "Google Gmail OAuth": r"[0-9]+-[0-9A-Za-z_]{32}\\.apps\\.googleusercontent\\.com",
    "Google OAuth Access Token": r"ya29\\.[0-9A-Za-z\\-_]+",
    "Google YouTube API Key": r"AIza[0-9A-Za-z\\-_]{35}",
    "Google YouTube OAuth": r"[0-9]+-[0-9A-Za-z_]{32}\\.apps\\.googleusercontent\\.com",
    'GitHub Access Token' : r'[a-zA-Z0-9_-]*:[a-zA-Z0-9_\-]+@github\.com*',
    "GitHub Personal Access Token": r"ghp_[0-9a-zA-Z]{36}",
    "GitHub URL": r"(?i)github.*['|\"][0-9a-zA-Z]{35,40}['|\"]",
    "GitHub App Token": r"(ghu|ghs)_[0-9a-zA-Z]{36}",
    "Slack Token": r"(xox[p|b|o|a]-[0-9]{12}-[0-9]{12}-[0-9]{12}-[a-z0-9]{32})",
    "Slack Webhook": r"https://hooks.slack.com/services/T\w{8}/B\w{8}/\w{24}",
    "Slack Webhook 2": r"T[a-zA-Z0-9_]{8}/B[a-zA-Z0-9_]{8}/[a-zA-Z0-9_]{24}",
    "Slack OAuth v2 Username/Bot Access Token": r"xoxb-[0-9]{11}-[0-9]{11}-[0-9a-zA-Z]{24}",
    "Slack OAuth v2 Configuration Token": r"xoxe.xoxp-1-[0-9a-zA-Z]{166}",
    "Picatic API Key": r"sk_live_[0-9a-z]{32}",
    "Stripe API Key": r"sk_live_[0-9a-zA-Z]{24}",
    "Stripe Restricted API Key": r"rk_live_[0-9a-zA-Z]{24}",
    "Twitter Access Token": r"(?i)twitter.*[1-9][0-9]+-\w{40}",
    "Twitter OAuth": r"(?i)twitter.*['|\"]\w{35,44}['|\"]",
    "Twitter Client ID": r"(?i)twitter(.{0,20})?['\"][0-9a-z]{18,25}",
    "URL Parameter": r"(?<=\?|\&)[a-zA-Z0-9_]+(?=\=)",
    "Twilio API Key": r"SK[0-9a-fA-F]{32}",
    "Square Access Token": r"sq0atp-[0-9A-Za-z\\-_]{22}",
    "Square OAuth Secret": r"sq0csp-[0-9A-Za-z\\-_]{43}",
    "URL": r'(https?|ftp)://(-\.)?([^\s/?\.#-]+\.?)+(/[^\s]*)?$iS',
    "Adobe Client Secret": r'''(?i)\b((p8e-)[a-zA-Z0-9]{32})(?:['|\"|\n|\r|\s|\x60]|$)''',
    "Alibaba AccessKey ID": r"(?i)\b((LTAI)[a-zA-Z0-9]{20})(?:['|\"|\n|\r|\s|\x60]|$)",
    "Clojars API Token": r"(?i)(CLOJARS_)[a-z0-9]{60}",
    "Doppler API Token": r"(dp\.pt\.)[a-zA-Z0-9]{43}",
    "Dynatrace API Token": r"dt0c01\.[a-zA-Z0-9]{24}\.[a-z0-9]{64}",
    "EasyPost API Token": r"EZAK[a-zA-Z0-9]{54}",
    "GitLab Personal Access Token": r"glpat-[0-9a-zA-Z\-\_]{20}",
    "NPM Access Token": r"(?i)\b(npm_[a-z0-9]{36})(?:['|\"|\n|\r|\s|\x60]|$)",
    "Shopify Private APP Access Token": r"shppa_[a-fA-F0-9]{32}",
    "Shopify Shared Secret": r"shpss_[a-fA-F0-9]{32}",
    "Shopify Custom Access Token": r"shpca_[a-fA-F0-9]{32}",
    "Shopify Access Token": r"shpat_[a-fA-F0-9]{32}",
    "Asana Client ID": r"""(?i)(?:asana)(?:[0-9a-z\-_\t .]{0,20})(?:[\s|']|[\s|"]){0,3}(?:=|>|:=|\|\|:|<=|=>|:)(?:'|\"|\s|=|\x60){0,5}([0-9]{16})(?:['|\"|\n|\r|\s|\x60|;]|$)""",
    "Asana Client Secret": r"""(?i)(?:asana)(?:[0-9a-z\-_\t .]{0,20})(?:[\s|']|[\s|"]){0,3}(?:=|>|:=|\|\|:|<=|=>|:)(?:'|\"|\s|=|\x60){0,5}([a-z0-9]{32})(?:['|\"|\n|\r|\s|\x60|;]|$)"""
 }

def direct_scan(link) -> None:
    " Open JavaScript file without parsing URL before requesting "
    
    response: function = get(link, **props, timeout=30)
    content: str = response.text
    content: str = beautify(content)

    for key, value in regex_list.items():
        pattern = value
        match = findall(pattern, content)

        if(match):
            print(f"\n[bold green][+] {key} found in {link} ~ [red]{match}[/][/]\n")

def passed_scan(final_url):
    " Parse the URL before open JavaScript directly "

    response: function = get(final_url, **props, timeout=30)
    content: str = response.text
    content: str = beautify(content)

    for key, value in regex_list.items():
        pattern = value
        match = findall(pattern, content)

        if(match):
            print(f"\n[bold green][+] {key} found in {final_url} ~ [red]{match}[/][/]\n")
