from colors import Success
import json
import sys


class ProgressBar:
    def __init__(self,
                 iterable=None,
                 length=25,
                 fill_char="▒",
                 empty_char=" ",
                 spinner="dots12"):
        self.length = length
        self.iterable = iterable
        self.n_items = len(iterable)
        self.fill_char = fill_char
        self.bar = [empty_char] * length
        self.entered = False
        self.current_item = iterable[0]
        self.index = 0
        self.iter = range(self.n_items)
        self.percent = 0
        with open('assets/spinners.json', 'rb') as f:
            spinners = json.load(f)
        self.spinner = spinners[spinner]

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

    def render_progress(self):
        text = Success(f"\r{''.join(self.bar)} {self.percent}% {self.spinner[self.index % len(self.spinner)]}")
        sys.stdout.write(str(text))
        sys.stdout.flush()

    def generator(self):
        for rv in self.iterable:
            self.current_item = rv
            yield rv
            self.update()

    def update(self):
        nbars = int((self.percent*0.01) * self.length)
        self.bar[nbars] = self.fill_char
        self.percent = round((self.index / self.n_items) * 100, 2)
        self.index += 1
        self.render_progress()

    def render_finish(self):
        self.current_item = None
        self.percent = 100
        self.render_progress()
        sys.stdout.write("\n")
