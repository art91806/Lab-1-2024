import time
import sys


SET_COLOR = "\x1b[48;5;"
END = "\x1b[0m"
CLEAR = "\033[H"


def draw_line(offset=0, length=1, color=222):
    line = " " * length
    print(f"{' ' * offset}{SET_COLOR}{color}m{line}{END}")


def draw_redwhite(offset=0, length=10):
    offset = ' ' * offset
    sys.stdout.write(f'{offset}' + '\u001b[41m'.ljust(length) + '\u001b[40m'.ljust(length) + '\u001b[47m'.ljust(length))
    print(f"{END}")


def draw_circle():

    size = 10
    radius = size // 2
    center = size // 2
    offset = size

    step = 1
    length = 1

    # print(size, center, offset)

    colors = [1, 7]

    while True:
        for line in range(size):
            draw_redwhite(offset, length)

            if line < center:
                offset -= step * 2
                length += step * 4
            else:
                offset += step * 2
                length -= step * 4
                

        print(f"\x1b[{size+2}A")
        print(f"\x1b[{offset}D")

        length = 2
        offset = size

        time.sleep(0.5)



if __name__ == "__main__":
    draw_circle()