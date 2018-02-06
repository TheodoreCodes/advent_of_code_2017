instructions = [int(x) for x in open("inputs/5.in").readlines()]


def solve(is_part_2):
    i = 0
    counter = 0
    while 0 <= i < len(instructions):
        prev = i
        i += instructions[i]
        if instructions[prev] >= 3 and is_part_2:
            instructions[prev] -= 1
        else:
            instructions[prev] += 1
        counter += 1
    return counter


print("Part 1: {}".format(solve(False)))
print("Part 2: {}".format(solve(True)))
