from colorama import Fore, Back, Style
import colorama
colorama.init()


class Red:
    def __init__(self, text, ground="fore"):
        self.text = text
        self.ground = ground

    def __str__(self):
        if self.ground == "back":
            return Back.LIGHTRED_EX + self.text + Style.RESET_ALL
        return Fore.LIGHTRED_EX + self.text + Style.RESET_ALL


class LightRed:
    def __init__(self, text, ground="fore"):
        self.text = text
        self.ground = ground

    def __str__(self):
        if self.ground == "back":
            return Back.LIGHTRED_EX + self.text + Style.RESET_ALL
        return Fore.LIGHTRED_EX + self.text + Style.RESET_ALL


class Green:
    def __init__(self, text, ground="fore"):
        self.text = text
        self.ground = ground

    def __str__(self):
        if self.ground == "back":
            return Back.GREEN + self.text + Style.RESET_ALL
        return Fore.GREEN + self.text + Style.RESET_ALL


class LightGreen:
    def __init__(self, text, ground="fore"):
        self.text = text
        self.ground = ground

    def __str__(self):
        if self.ground == "back":
            return Back.LIGHTGREEN_EX + self.text + Style.RESET_ALL
        return Fore.LIGHTGREEN_EX + self.text + Style.RESET_ALL


class Blue:
    def __init__(self, text, ground="fore"):
        self.text = text
        self.ground = ground

    def __str__(self):
        if self.ground == "back":
            return Back.BLUE + self.text + Style.RESET_ALL
        return Fore.BLUE + self.text + Style.RESET_ALL


class LightBlue:
    def __init__(self, text, ground="fore"):
        self.text = text
        self.ground = ground

    def __str__(self):
        if self.ground == "back":
            return Back.LIGHTBLUE_EX + self.text + Style.RESET_ALL
        return Fore.LIGHTBLUE_EX + self.text + Style.RESET_ALL


class Yellow:
    def __init__(self, text, ground="fore"):
        self.text = text
        self.ground = ground

    def __str__(self):
        if self.ground == "back":
            return Back.YELLOW + self.text + Style.RESET_ALL
        return Fore.YELLOW + self.text + Style.RESET_ALL


class LightYellow:
    def __init__(self, text, ground="fore"):
        self.text = text
        self.ground = ground

    def __str__(self):
        if self.ground == "back":
            return Back.LIGHTYELLOW_EX + self.text + Style.RESET_ALL
        return Fore.LIGHTYELLOW_EX + self.text + Style.RESET_ALL


class Magenta:
    def __init__(self, text, ground="fore"):
        self.text = text
        self.ground = ground

    def __str__(self):
        if self.ground == "back":
            return Back.MAGENTA + self.text + Style.RESET_ALL
        return Fore.MAGENTA + self.text + Style.RESET_ALL


class LightMagenta:
    def __init__(self, text, ground="fore"):
        self.text = text
        self.ground = ground

    def __str__(self):
        if self.ground == "back":
            return Back.LIGHTMAGENTA_EX + self.text + Style.RESET_ALL
        return Fore.LIGHTMAGENTA_EX + self.text + Style.RESET_ALL


class Cyan:
    def __init__(self, text, ground="fore"):
        self.text = text
        self.ground = ground

    def __str__(self):
        if self.ground == "back":
            return Back.CYAN + self.text + Style.RESET_ALL
        return Fore.CYAN + self.text + Style.RESET_ALL


class LightCyan:
    def __init__(self, text, ground="fore"):
        self.text = text
        self.ground = ground

    def __str__(self):
        if self.ground == "back":
            return Back.LIGHTCYAN_EX + self.text + Style.RESET_ALL
        return Fore.LIGHTCYAN_EX + self.text + Style.RESET_ALL


class Black:
    def __init__(self, text, ground="fore"):
        self.text = text
        self.ground = ground

    def __str__(self):
        if self.ground == "back":
            return Back.BLACK + self.text + Style.RESET_ALL
        return Fore.BLACK + self.text + Style.RESET_ALL


class LightBlack:
    def __init__(self, text, ground="fore"):
        self.text = text
        self.ground = ground

    def __str__(self):
        if self.ground == "back":
            return Back.LIGHTBLACK_EX + self.text + Style.RESET_ALL
        return Fore.LIGHTBLACK_EX + self.text + Style.RESET_ALL


class White:
    def __init__(self, text, ground="fore"):
        self.text = text
        self.ground = ground

    def __str__(self):
        if self.ground == "back":
            return Back.WHITE + self.text + Style.RESET_ALL
        return Fore.WHITE + self.text + Style.RESET_ALL


class LightWhite:
    def __init__(self, text, ground="fore"):
        self.text = text
        self.ground = ground

    def __str__(self):
        if self.ground == "back":
            return Back.LIGHTWHITE_EX + self.text + Style.RESET_ALL
        return Fore.LIGHTWHITE_EX + self.text + Style.RESET_ALL


class Error:
    def __init__(self, text):
        print("\n[-] " + Fore.LIGHTRED_EX + text + Style.RESET_ALL)


class Success:
    def __init__(self, text):
        print("\n[*] " + Fore.LIGHTCYAN_EX + text + Style.RESET_ALL)


class Warn:
    def __init__(self, text):
        print("\n[!] " + Fore.LIGHTYELLOW_EX + text + Style.RESET_ALL)
