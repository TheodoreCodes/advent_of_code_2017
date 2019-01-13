with open('inputs/2.in') as f:
    ids = [x.strip() for x in f.readlines()]

def part_1():
    count_2 = count_3 = 0
    for id in ids:
        stop_3: bool = False
        stop_2: bool = False

        for l in id:
            if id.count(l) == 3 and not stop_3:
                count_3 += 1
                stop_3 = True
            elif id.count(l) == 2 and not stop_2:
                count_2 += 1
                stop_2 = True
            id.replace(l, '')

        if not stop_2 and not stop_3:
            ids.remove(id)

    return count_2 * count_3


def part_2():
    for id1 in ids:
        for id2 in ids:
            common = ''.join(a for a, b in zip(id1, id2) if a == b)
            if len(common) == len(id1) - 1:
                return common


if __name__ == '__main__':
    print(part_1())
    print(part_2())
