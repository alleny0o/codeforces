t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    outcome = "YES"  # Assume the outcome is YES initially

    if sum(arr) % 4 != 0:
        print("NO")
        continue  # Skip to the next test case

    for i in range(2, n):
        min_ops = min(arr[i], arr[i-1]//2, arr[i-2])
        arr[i] -= min_ops
        arr[i-1] -= min_ops * 2
        arr[i-2] -= min_ops

        # Check if any operation made an element negative
        if arr[i] < 0 or arr[i-1] < 0 or arr[i-2] < 0:
            outcome = "NO"
            break  # Exit the loop since we found a NO condition

    # If the loop completes without changing the outcome to NO, check final array condition
    if outcome == "YES" and not (all(x <= 0 for x in arr) and sum(arr) == 0):
        outcome = "NO"

    print(outcome)
