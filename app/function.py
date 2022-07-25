OK = '\033[92m' # Green
WARNING = '\033[33m' # Orange
FAIL = '\033[91m' # Red
INFO = '\033[90m' # gray
RESET = '\033[0m' # white
BLUE = '\033[34m' # blue
CYAN = '\033[36m' # cyan
YELLOW = '\033[93m' # yellow

class Color():
    @staticmethod
    def print_ok(message: str):
        print("{}[+] {} {}".format(OK, message, RESET))
    
    def print_warning(message: str):
        print("{}[/] {} {}".format(WARNING, message, RESET))

    def print_fail(message: str):
        print("{}[-] {} {}".format(FAIL, message, RESET))

    def print_info(message: str):
        print("{}[::info::] {} {}".format(INFO, message, RESET))
