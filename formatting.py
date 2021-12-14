

class Header:
    def __init__(self, text):
        print(text)
        print("=" * len(text))


class Tabbed:
    def __init__(self, text, tabs=1):
        print("\t"*tabs+text)
