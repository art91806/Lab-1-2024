import sys


RED = '\u001b[41m'
WHITE = '\u001b[47m'
SET_COLOR = "\x1b[48;5;"
END = "\x1b[0m"
CLEAR = "\033[H"


def draw_line(offset=0, length=15):
    line = " " * length
    print(f"{' ' * offset}{RED}{line}{END}")

def draw_redwhite(offset=0, length=10):
    sys.stdout.write('\u001b[41m'.ljust(length) + '\u001b[47m'.ljust(length) + '\u001b[41m'.ljust(length))
    print(f"{END}")


def draw_whitelong(offset=0, length=10):
    lred = length // 2 + 1
    lwhite = length * 2 - 2
    sys.stdout.write('\u001b[41m'.ljust(lred) + '\u001b[47m'.ljust(lwhite) + '\u001b[41m'.ljust(lred))
    print(f"{END}")


if __name__ == "__main__":
    for i in range(8):
        if i == 0 or i == 7:
            draw_line()
        elif 1 <= i <= 2 or 5 <= i <= 6:
            draw_redwhite()
        else:
            draw_whitelong()