import re
import string

def dance(progs, move):
    move = re.search('(s|x|p)([a-p0-9]+)/?([a-p0-9]+)?', move)
    if move.group(1) == 's':
        i = int(move.group(2))
        while i > 0:
            progs.insert(0, progs.pop())
            i -= 1

    else:
        if move.group(1) == 'x':
            a = int(move.group(2))
            b = int(move.group(3))

        if move.group(1) == 'p':
            a = progs.index(move.group(2))
            b = progs.index(move.group(3))

        progs[a], progs[b] = progs[b], progs[a]


programs = list(string.ascii_lowercase[:16])
results = [list(programs)]


def part_1():
    for x in open("inputs/16.in").read().split(","):
        dance(programs, x)


part_1()
print("First part:", "".join(programs))

while programs != results[0]:
    results.append(list(programs))
    part_1()

index = 1000000000 % len(results)
print("Second part:", "".join(results[index]))
