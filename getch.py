class _Getch:
    """Gets a single character from standard input.  Does not echo to the screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self):
        return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()

# from time import sleep
# import threading
# ready = threading.Event()
#
#
# def inp():
#     while True:
#         c = getch()
#         if c == ' ':
#             print("yes")
#             if ready.is_set():
#                 ready.clear()
#             else:
#                 ready.set()
#         if c == 'q':
#             break
#
#
# k = threading.Thread(target=inp)
# k.start()
#
# ready.set()
# for i in range(15):
#     ready.wait()
#     sleep(1)
#     print('k')


