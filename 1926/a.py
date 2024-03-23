for _ in range(int(input())):
    s: str = input()
    d: dict = {'A': 0, 'B': 0}
    for letter in s:
        if letter == 'A':
            d['A'] = d['A'] + 1
        elif letter == 'B':
            d['B'] = d['B'] + 1

    if d['A'] > d['B']:
        print('A')
    else:
        print('B')
