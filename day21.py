import numpy as np


def str_to_nparray(string):
    rule = string.split("/")
    s = len(rule)
    return np.array([list(row[x:x + s]) for row in rule for x in range(0, s, s)])


def match(m1, m2):
    temp = m1
    for _ in range(8):
        if not np.array_equal(temp, m2):
            temp = np.transpose(temp) if _ % 2 == 0 else np.fliplr(temp)
        else:
            return True

    return False


def divide(m):
    l = 2 if len(m) % 2 == 0 else 3
    sections = [[y for y in range(x, x + l)] for x in range(0, len(m), l)]

    return [m[np.ix_(i, j)] for i in sections for j in sections]


def concat(m_arr):
    if len(m_arr) > 1:
        rows = []
        side = int(len(m_arr)**(1/2))
        for i in range(0, len(m_arr), side):
            rows.append(m_arr[i:i+side])

        return np.block(rows)
    else:
        return m_arr[0]


cookbook = []
for line in open("inputs/21.in").readlines():
    line = line.split(" => ")
    cookbook.append((
        str_to_nparray(line[0]),
        str_to_nparray(line[1])
    ))

pattern = str_to_nparray(".#./..#/###")

for _ in range(5):
    pattern = divide(pattern)
    for i, m in enumerate(pattern):
        for rule in cookbook:
            if match(m, rule[0]):
                pattern[i] = rule[1]
                break
    pattern = concat(pattern)

print("First part:", (pattern == '#').sum())

for _ in range(13):
    pattern = divide(pattern)
    for i, m in enumerate(pattern):
        for rule in cookbook:
            if match(m, rule[0]):
                pattern[i] = rule[1]
                break
    pattern = concat(pattern)

print("Second part:", (pattern == '#').sum())
