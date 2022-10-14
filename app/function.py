import platform, os
from banner import Banner

OK = '\033[92m' # Green
WARNING = '\033[33m' # Orange
FAIL = '\033[91m' # Red
INFO = '\033[90m' # gray
RESET = '\033[0m' # white
BLUE = '\033[34m' # blue
CYAN = '\033[36m' # cyan
YELLOW = '\033[93m' # yellow

SYSTEM = platform.system()
CLEAR = "cls" if SYSTEM.lower() == "windows" else "clear"

class Print:
    @staticmethod
    def ok(message: str):
        print("{}[+] {} {}".format(OK, message, RESET))

    @staticmethod
    def warning(message: str):
        print("{}[?] {} {}".format(WARNING, message, RESET))

    @staticmethod
    def fail(message: str):
        print("{}[-] {} {}".format(FAIL, message, RESET))

    @staticmethod
    def info(message: str):
        print("{}[::info::] {} {}".format(INFO, message, RESET))

    @staticmethod
    def banner():
        print(Banner())
        print("{}[Author] => Daniel Mantilla Cóndor {}".format(CYAN, RESET))
        print("{}[Site..] => https://github.com/DanielMCondor {}".format(CYAN, RESET))
        print("")

class Clear:
    def __init__(self):
        os.system(CLEAR)