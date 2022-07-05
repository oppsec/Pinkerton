from src.interface.ui import banner
from src.pinkerton.main import check_host

from argparse import ArgumentParser

if __name__ == "__main__":
    
    banner()

    parser = ArgumentParser(description="List of arguments that can be passed in Pinkerton")
    parser.add_argument("-u", help="Specify the target URL", required=False)
    #parser.add_argument("-l", help="Specify a file with a list of URLs", required=False)
    args = parser.parse_args()

    check_host(args)
