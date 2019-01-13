from day10 import solve, dense_hash

INPUT = "hxtvlmkl"

ones = set()
for row_no in range(128):
    inp = [ord(c) for c in "{}-{}".format(INPUT, row_no)]
    inp.extend([17, 31, 73, 47, 23])
    reverse = solve(64, inp)
    dense_hash(0, 15, reverse)
    bin_row = [b for x in reverse for y in hex(x)[2:].zfill(2) for z in y for b in bin(int(z, 16))[2:].zfill(4)]
    for k, v in enumerate(bin_row):
        if v == '1':
            ones.add((row_no, k))


def part_1():
    return len(ones)


directions = ((1, 0), (0, -1), (-1, 0), (0, 1))


def find_regions(one):
    stack = [one]
    while stack:
        (x, y) = stack.pop()
        for dx, dy in directions:
            neighbour = (x + dx, y + dy)
            if neighbour in ones:
                stack.append(neighbour)
                ones.remove(neighbour)


def part_2():
    regions = 0
    while ones:
        find_regions(ones.pop())
        regions += 1

    return regions


print("Part 1:", part_1())
print("Part 2:", part_2())
