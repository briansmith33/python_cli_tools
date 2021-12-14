import typer
from datetime import datetime, date
import keyboard
import mouse
import time
import winsound
import calendar
import json
import requests
import colorama
from colorama import Fore
import argparse
from prompt_toolkit import prompt, HTML, ANSI
# from prompt_toolkit import print_formatted_text as print
from string import ascii_lowercase, ascii_letters, punctuation
import textwrap
import sys
import ctypes
import psutil
import os
import random
from base64 import b64encode, b64decode
import ast
colorama.init(autoreset=True)


class Progress:
    def __init__(self,
                 iterable=None,
                 length=25,
                 end_char="[]",
                 fill_char="#",
                 empty_char=" ",
                 color=None,
                 spinner=None,
                 show_progress=True,
                 show_percent=False):
        self.iterable = iterable
        self.n_items = len(iterable)
        self.end_char = end_char
        self.fill_char = fill_char
        self.bar = [empty_char] * length
        self.entered = False
        self.current_item = iterable[0]
        self.index = 0
        self.iter = range(self.n_items)
        self.step_size = int(len(iterable) / length)
        self.step = 0
        self.spinner_step = 0
        self.color = color
        self.percent = 0
        self.spinner = spinner
        self.spinners = self.get_spinners()
        self.show_progress = show_progress
        self.show_percent = show_percent
        self.colors = {
            "black": Fore.BLACK,
            "red": Fore.RED,
            "green": Fore.GREEN,
            "yellow": Fore.YELLOW,
            "blue": Fore.BLUE,
            "magenta": Fore.MAGENTA,
            "cyan": Fore.CYAN
        }

    def __enter__(self):
        self.entered = True
        self.render_progress()
        return self

    def __exit__(self, exc_type, exc_value, tb):
        self.render_finish()

    def __iter__(self):
        if not self.entered:
            raise RuntimeError("You need to use progress bars in a with block.")
        self.render_progress()
        return self.generator()

    def __next__(self):
        return next(iter(self))

    @staticmethod
    def get_spinners():
        with open("spinners.json", "rb") as f:
            return json.load(f)

    def render_progress(self):
        if self.color is not None:
            if self.show_progress:
                if self.end_char == "":
                    sys.stdout.write(f"\r{self.colors[self.color]}{''.join(self.bar)}")
                else:
                    sys.stdout.write(
                        f"\r{self.colors[self.color]}{self.end_char[0]}{''.join(self.bar)}{self.end_char[1]}")

            if self.show_percent:
                sys.stdout.write(f"\r {self.colors[self.color]}{self.percent}%")

            if self.spinner is not None:
                spinner = self.spinners[self.spinner]
                sys.stdout.write(f"\r {self.colors[self.color]}{spinner[self.spinner_step]}")
                if self.spinner_step < len(spinner) - 1:
                    self.spinner_step += 1
                else:
                    self.spinner_step = 0

            if self.show_progress and self.show_percent:
                if self.end_char == "":
                    sys.stdout.write(f"\r{self.colors[self.color]}{''.join(self.bar)} {self.percent}%")
                else:
                    sys.stdout.write(
                        f"\r{self.colors[self.color]}{self.end_char[0]}{''.join(self.bar)}{self.end_char[1]} {self.percent}%")

            if not self.show_progress and self.show_percent and self.spinner is not None:
                spinner = self.spinners[self.spinner]
                sys.stdout.write(f"\r{self.colors[self.color]}{spinner[self.spinner_step]} {self.percent}%")
                if self.spinner_step < len(spinner) - 1:
                    self.spinner_step += 1
                else:
                    self.spinner_step = 0

            if self.show_progress and self.show_percent and self.spinner is not None:
                spinner = self.spinners[self.spinner]
                if self.end_char == "":
                    sys.stdout.write(
                        f"\r{self.colors[self.color]}{spinner[self.spinner_step]} {''.join(self.bar)} {self.percent}%")
                else:
                    sys.stdout.write(
                        f"\r{self.colors[self.color]}{spinner[self.spinner_step]} {self.end_char[0]}{''.join(self.bar)}{self.end_char[1]} {self.percent}%")
                if self.spinner_step < len(spinner) - 1:
                    self.spinner_step += 1
                else:
                    self.spinner_step = 0
        else:
            if self.show_progress:
                if self.end_char == "":
                    sys.stdout.write(f"\r{''.join(self.bar)}")
                else:
                    sys.stdout.write(f"\r{self.end_char[0]}{''.join(self.bar)}{self.end_char[1]}")

            if self.show_percent:
                sys.stdout.write(f"\r {self.percent}%")

            if self.spinner is not None:
                spinner = self.spinners[self.spinner]
                sys.stdout.write(f"\r {spinner[self.spinner_step]}")
                if self.spinner_step < len(spinner) - 1:
                    self.spinner_step += 1
                else:
                    self.spinner_step = 0

            if self.show_progress and self.show_percent:
                if self.end_char == "":
                    sys.stdout.write(f"\r{''.join(self.bar)} {self.percent}%")
                else:
                    sys.stdout.write(f"\r{self.end_char[0]}{''.join(self.bar)}{self.end_char[1]} {self.percent}%")

            if not self.show_progress and self.show_percent and self.spinner is not None:
                spinner = self.spinners[self.spinner]
                sys.stdout.write(f"\r{spinner[self.spinner_step]} {self.percent}%")
                if self.spinner_step < len(spinner) - 1:
                    self.spinner_step += 1
                else:
                    self.spinner_step = 0

            if self.show_progress and self.show_percent and self.spinner is not None:
                spinner = self.spinners[self.spinner]
                if self.end_char == "":
                    sys.stdout.write(
                        f"\r{spinner[self.spinner_step]} {''.join(self.bar)} {self.percent}%")
                else:
                    sys.stdout.write(
                        f"\r{spinner[self.spinner_step]} {self.end_char[0]}{''.join(self.bar)}{self.end_char[1]} {self.percent}%")
                if self.spinner_step < len(spinner) - 1:
                    self.spinner_step += 1
                else:
                    self.spinner_step = 0

        sys.stdout.flush()

    def generator(self):
        for rv in self.iterable:
            self.current_item = rv
            yield rv
            self.update(self.index)

    def update(self, value):
        if value % self.step_size == 0:
            if self.step < len(self.bar):
                self.bar[self.step] = self.fill_char
            self.step += 1
            self.percent = round((self.index / self.n_items) * 100, 2)
        self.index += 1
        self.render_progress()

    def render_finish(self):
        self.current_item = None
        self.percent = 100
        self.render_progress()


'''
print("[*] Welcome\n")
print("Starting services...")
todos = random.choices(ascii_letters + digits, k=100)
with Progress(todos,
              end_char="",
              fill_char="▓",
              empty_char="░",
              spinner="clock",
              color="cyan",
              show_percent=True) as p:

    for _ in p:
        sys.stdout.write(f"\t{p.current_item}")
        sys.stdout.flush()
        time.sleep(0.1)
'''

'''
print(HTML('<b>This is bold</b>'))
print(HTML('<i>This is italic</i>'))
print(HTML('<u>This is underlined</u>'))
print(HTML('<ansired>This is red</ansired>'))
print(HTML('<ansigreen>This is green</ansigreen>'))

# Named colors (256 color palette, or true color, depending on the output).
print(HTML('<skyblue>This is sky blue</skyblue>'))
print(HTML('<seagreen>This is sea green</seagreen>'))
print(HTML('<violet>This is violet</violet>'))
print(HTML('<aaa fg="ansiwhite" bg="ansigreen">White on green</aaa>'))
from prompt_toolkit.styles import Style

style = Style.from_dict({
    'aaa': '#ff0066',
    'bbb': '#44ff00 italic',
})

print(HTML('<aaa>Hello</aaa> <bbb>world</bbb>!'), style=style)
print(ANSI('\x1b[31mhello \x1b[32mworld'))

from prompt_toolkit.formatted_text import FormattedText

text = FormattedText([
    ('#ff0066', 'Hello'),
    ('', ' '),
    ('#44ff00 italic', 'World'),
])

print(text)

# The text.
text = FormattedText([
    ('class:aaa', 'Hello'),
    ('', ' '),
    ('class:bbb', 'World'),
])

# The style sheet.
style = Style.from_dict({
    'aaa': '#ff0066',
    'bbb': '#44ff00 italic',
})

print(text, style=style)
from pygments.token import Token
from prompt_toolkit.formatted_text import PygmentsTokens

text = [
    (Token.Keyword, 'print'),
    (Token.Punctuation, '('),
    (Token.Literal.String.Double, '"'),
    (Token.Literal.String.Double, 'hello'),
    (Token.Literal.String.Double, '"'),
    (Token.Punctuation, ')'),
    (Token.Text, '\n'),
]

print(PygmentsTokens(text))
from prompt_toolkit import Application
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.layout.containers import VSplit, Window
from prompt_toolkit.layout.controls import BufferControl, FormattedTextControl
from prompt_toolkit.layout.layout import Layout

buffer1 = Buffer()  # Editable buffer.

root_container = VSplit([
    # One window that holds the BufferControl with the default buffer on
    # the left.
    Window(content=BufferControl(buffer=buffer1)),

    # A vertical line in the middle. We explicitly specify the width, to
    # make sure that the layout engine will not try to divide the whole
    # width by three for all these windows. The window will simply fill its
    # content by repeating this character.
    Window(width=1, char='|'),

    # Display the text 'Hello world' on the right.
    Window(content=FormattedTextControl(text='Hello world')),
])

layout = Layout(root_container)

app = Application(layout=layout, full_screen=True)
app.run() # You won't be able to Exit this app

#
#print(win32gui.SetFocus(win32gui.GetForegroundWindow()))
#print(win32gui.GetFocus())

'''


class Argument:
    def __init__(self, name):
        self.name = name


class Parser:
    def __init__(self, description=None):
        self.description = description
        self.arguments = []


if __name__ == "__main__":
    '''
    print("\u0332".join("X "))
    p = psutil.Process()

    with p.oneshot():
        print(psutil.cpu_count())
        print(p.memory_info())
        print(p.memory_maps())
        print(p.open_files())

        print(psutil.virtual_memory())
        print(psutil.swap_memory())
        print(psutil.disk_usage('/'))
        print(psutil.disk_io_counters())
        print(psutil.net_io_counters())
        print(psutil.net_connections())
        print(psutil.net_if_stats())
        print(psutil.sensors_battery())
        print(psutil.boot_time())
    underline_byte = b'\xcc\xb2'
    underline = str(underline_byte, 'utf-8')
    print("X"+underline, end="")
    '''

    print(phone_verify("12104830225"))
