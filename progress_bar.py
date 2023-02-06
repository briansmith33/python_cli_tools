from colorama import Fore, Back, Style
import colorama
import json
import sys
colorama.init()


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