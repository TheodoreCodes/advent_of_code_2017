A_FACTOR = 16807
B_FACTOR = 48271
DIVIDER = 2147483647

# def generator(value, factor)

def part_1(a_val, b_val):
    total = 0
    for _ in range(40000000):
        a_val = (a_val * A_FACTOR) % DIVIDER
        b_val = (b_val * B_FACTOR) % DIVIDER
        total += 1 if bin(a_val)[2:].zfill(32)[-16:] == bin(b_val)[2:].zfill(32)[-16:] else 0

    return total

def part_2(a_val, b_val):
    total = 0
    counter = 0
    matches = [False, False]
    while counter < 5000000:
        if not matches[0]:
            a_val = (a_val * A_FACTOR) % DIVIDER
            matches[0] = True if a_val % 4 == 0 else False

        if not matches[1]:
            b_val = (b_val * B_FACTOR) % DIVIDER
            matches[1] = True if b_val % 8 == 0 else False

        if sum(matches) == 2:
            total += 1 if bin(a_val)[2:].zfill(32)[-16:] == bin(b_val)[2:].zfill(32)[-16:] else 0
            counter += 1
            matches = [False, False]

    return total


# print("First part", part_1(883, 879))

print("Second part", part_2(883, 879))