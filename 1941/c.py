def min_removals_for_beautiful_string(test_cases):
    results = []

    for n, s in test_cases:
        i = 0
        removals = 0
        while i < n:
            if i + 2 < n and (s[i:i+3] == "pie" or s[i:i+3] == "map"):
                removals += 1
                i += 3  # Skip the current substring since we're removing one char from it
            else:
                i += 1
        results.append(removals)

    return results


# Input
t = int(input().strip())
test_cases = []
for _ in range(t):
    n = int(input().strip())
    s = input().strip()
    test_cases.append((n, s))

# Processing
results = min_removals_for_beautiful_string(test_cases)

# Output
for result in results:
    print(result)
