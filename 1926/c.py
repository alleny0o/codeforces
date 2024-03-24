totals = [0] * 200001
for i in range(1, 200001):
    sub = 0
    curr = i
    while curr > 0:
        sub += curr % 10
        curr //= 10
    totals[i] = totals[i-1] + sub

for _ in range(int(input())):
    n = int(input())
    print(totals[n])
