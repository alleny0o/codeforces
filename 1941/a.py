for _ in range(int(input())):
    n, m, k = map(int, input().split())

    left_pocket = list(map(int, input().split()))
    right_pocket = list(map(int, input().split()))

    count = 0
    for i in left_pocket:
        for j in right_pocket:
            if i + j <= k:
                count = count + 1

    print(count)
