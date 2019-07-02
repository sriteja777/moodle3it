import msvcrt

while True:
    l = msvcrt.getch()
    print(l)
    if l.decode('utf-8') == 'p':
        break
