import re
from collections import defaultdict

with open('inputs/3.in') as f:
    claims = [x.strip() for x in f.readlines()]

fabric = defaultdict(set)
ids = set()

for c in claims:
    claim_id, x, y, w, h = map(int, re.findall(r'\d+', c))
    ids.add(claim_id)

    for i in range(x, x + w):
        for j in range(y, y + h):
            fabric[(i, j)].add(claim_id)

if __name__ == '__main__':
    # Part 1
    print(sum([1 for x in fabric if len(fabric[x]) > 1]))

    # Part 2
    for f in fabric:
        if len(fabric[f]) > 1:
            ids = ids.difference(fabric[f])

    print(ids)
