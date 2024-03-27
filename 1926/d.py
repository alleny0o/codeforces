# Python is too slow...

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    cnt = {}
    answer = 0
    for x in a:
        target = (2**31 - 1) ^ x
        if target in cnt and cnt[target] > 0:
            answer += 1
            cnt[target] -= 1
            if cnt[target] == 0:
                del cnt[target]
        else:
            cnt[x] = cnt.get(x, 0) + 1
    print(answer + sum(cnt.values()))
