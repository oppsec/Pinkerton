from random import choice

def get_user_agent() -> str:
    " Return a random User-Agent from user-agents.txt file to be used on request "

    file_path: str = 'src/pinkerton/data/user-agents.txt'
    with open(file_path) as content:
        user_agents: str = content.readlines()
        user_agent: str = choice(user_agents).strip()

        return user_agent

headers = {
    'User-Agent': get_user_agent(),
    'Connection': 'keep-alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
}

props = { 
    'verify': False,
    'allow_redirects': True,
    'headers': headers
}
