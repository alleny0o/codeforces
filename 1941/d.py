t = int(input())  # Number of test cases
for _ in range(t):
    n, m, x = map(int, input().split())
    directions = [input().split() for _ in range(m)]

    # Initialize potential ball holders as a set containing only the starting player
    possible_holders = {x}

    for distance, direction in directions:
        distance = int(distance)
        new_possible_holders = set()

        # For each possible holder, compute new positions after the throw
        for holder in possible_holders:
            if direction == '?':
                # Clockwise
                new_possible_holders.add((holder + distance - 1) % n + 1)
                # Counterclockwise
                new_possible_holders.add((holder - distance - 1) % n + 1)
            elif direction == '0':
                # Clockwise
                new_possible_holders.add((holder + distance - 1) % n + 1)
            else:  # direction == '1'
                # Counterclockwise
                new_possible_holders.add((holder - distance - 1) % n + 1)

        possible_holders = new_possible_holders

    print(len(possible_holders))
    print(' '.join(map(str, sorted(possible_holders))))
