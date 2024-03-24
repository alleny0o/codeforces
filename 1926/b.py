for _ in range(int(input())):
    n: int = int(input())
    lines: list = []
    for row in range(n):
        line = input()
        lines.append(line)
    square = False
    d: dict = {}
    for idx, seq in enumerate(lines):
        d[idx] = 0
        for l in seq:
            if int(l) == 1:
                d[idx] = d[idx] + 1
        if idx > 0 and d[idx] > 0 and d[idx] == d[idx-1]:
            print("SQUARE")
            square = True
            break
    if not square:
        print("TRIANGLE")
