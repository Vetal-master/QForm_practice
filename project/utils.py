from colorama import init, Fore
from colorama import Back
from colorama import Style

init(autoreset=True)


def output_red_text(massage):
    print(Fore.RED + massage)


def output_green_text(massage):
    print(Fore.GREEN + massage)

