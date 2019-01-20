import re
from collections import defaultdict

tasks = set()
dependencies = defaultdict(list)
with open('inputs/7.in') as f:
    for line in f:
        a, b = re.findall(r' [A-Z] ', line)
        tasks |= {a, b}
        dependencies[b].append(a)

part_1 = []

for _ in tasks:
    part_1.append(min([x for x in tasks if x not in part_1 and set(part_1) >= set(dependencies[x])]))

print(''.join(map(lambda s: s.replace(" ", ""), part_1)))