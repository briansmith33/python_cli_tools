from string import ascii_letters, digits
from progress_bar import Progress
import colorama
import random
import time
import sys
colorama.init(autoreset=True)


if __name__ == "__main__":
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


