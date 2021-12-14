from colorama import Fore, Style
import colorama
import msvcrt
import sys
colorama.init()


class Question:
    def __init__(self, text):
        print("\n[~] " + Fore.LIGHTMAGENTA_EX + text + Style.RESET_ALL, end=": ")
        self.answer = input()


def blit(text):
    sys.stdout.write(f"\r{text}")
    sys.stdout.flush()


def getpass(prompt='Password: ', fill_char="*"):
    blit(prompt)
    pw = ""
    while True:
        c = msvcrt.getwch()
        msvcrt.putwch(c)
        if c == '\r' or c == '\n':
            break
        if c == '\003':
            raise KeyboardInterrupt
        if c == '\b':
            pw = pw[:-1]
            stars = fill_char * len(pw)
            blit(prompt + stars + " ")
            blit(prompt + stars)
        else:
            pw = pw + c
            stars = fill_char * len(pw)
            blit(prompt + stars)

    blit('\n')
    return pw


class Seq:
    def __init__(self, array):
        self.sequence = list(array)

    def __repr__(self):
        return self.sequence

    def __str__(self):
        return str(self.sequence)

    def map(self, func):
        return Seq(map(func, self.sequence))

    def filter(self, func):
        return Seq(list(filter(func, self.sequence)))
