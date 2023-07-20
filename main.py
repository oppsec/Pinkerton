from src.interface.ui import banner
from src.pinkerton.main import perform_checks

from argparse import ArgumentParser

if __name__ == "__main__":
    
    banner()

    parser = ArgumentParser(description="List of arguments that can be passed in Pinkerton")
    parser.add_argument("-u", help="Specify the target URL", required=True)
    args = parser.parse_args()

    perform_checks(args)
