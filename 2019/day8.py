with open('inputs/8.in') as f:
    tree = [int(x) for x in f.read().split()]


def parse(tree):
    children, metadata = tree[:2]
    tree = tree[2:]
    total = 0

    for _ in range(children):
        t, tree = parse(tree)
        total += t

    total += sum(tree[:metadata])

    return total, tree[metadata:]


total, _ = parse(tree)
print(total)
