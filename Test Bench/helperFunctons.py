import sys
from colorama import Fore, Back, Style, init


# Better print function with color and background options
def betterPrint(element: str, color: str = None, background: str = None, spacing: bool = True):
    # Convert color names to Back.(color) or the text equivalent for colorama
    color = color.upper() if color else "RESET"
    background = background.upper() if background else "RESET"

    

    color_dict = {
        "BLACK": Fore.BLACK,
        "RED": Fore.RED,
        "GREEN": Fore.GREEN,
        "YELLOW": Fore.YELLOW,
        "BLUE": Fore.BLUE,
        "MAGENTA": Fore.MAGENTA,
        "CYAN": Fore.CYAN,
        "WHITE": Fore.WHITE,
        "RESET": Fore.RESET
    }

    background_dict = {
        "BLACK": Back.BLACK,
        "RED": Back.RED,
        "GREEN": Back.GREEN,
        "YELLOW": Back.YELLOW,
        "BLUE": Back.BLUE,
        "MAGENTA": Back.MAGENTA,
        "CYAN": Back.CYAN,
        "WHITE": Back.WHITE,
        "RESET": Back.RESET
    }

    if color and background:
        if color not in color_dict.keys() or background not in background_dict.keys():
            print("Invalid color or background color")
            return False
    color = color_dict.get(color, '')
    background = background_dict.get(background, '')

    if spacing:
        print(" ")
        print(f"{background}{color}{element}{Style.RESET_ALL}")
        print(" ")
    else:
        print(f"{background}{color}{element}{Style.RESET_ALL}")

    return True

