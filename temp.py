from time import sleep
# from getch import _Getch
import threading

# ready = threading.Event()
ready = threading.Event()

def print_percentage():
    print('dsfsf ',end='', flush=True)
    sleep(1)
    k = '\b'
    for i in range(100):
        sleep(0.05)
        print('{0}% Completed'.format(i),'\b'*11, k.rjust(len(str(i)), '\b'), sep='', end='', flush=True)
    print(14*' ', 14*'\b', sep='', end='')
    print('dsfsf')


from readchar import readchar
from getch import getch
import os, signal
r = threading.Event()
def inp():
    while True:
        r.wait()
        c = readchar()

        if c == ' ':
            print("yes")
            if ready.is_set():
                ready.clear()
            else:
                ready.set()
        if c == 'q':
            break
        if c == '\x1a':
            os.kill(os.getpid(), signal.SIGTSTP)


k = threading.Thread(target=inp)
k.start()

ready.set()
for i in range(15):
    ready.wait()
    sleep(1)
    r.clear()
    print(i, sep='')
    r.set()
