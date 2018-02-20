from collections import defaultdict
from copy import copy

grid = defaultdict(int)
for j, line in enumerate(open("inputs/22.in").readlines()):
    for i, v in enumerate(line.strip("\n")):
        grid[(i, j)] = 2 if v == '#' else 0

initial = copy(grid)

pos = (len(line) // 2, len(line) // 2)
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
cur_dir = 0

infections = 0
for _ in range(10_000):
    cur_dir = (cur_dir + (-1 if grid[pos] == 0 else 1)) % 4
    grid[pos] = 2 if grid[pos] == 0 else 0
    infections += 1 if grid[pos] == 2 else 0
    pos = (pos[0] + directions[cur_dir][0], pos[1] + directions[cur_dir][1])

print("First part:", infections)

'''
0 - Clean
1 - Weakend
2 - Infected
3 - Flagged
'''
grid = initial
pos = (len(line) // 2, len(line) // 2)
infections = 0
cur_dir = 0

for _ in range(10_000_000):
    cur_dir = (cur_dir + grid[pos] - 1) % 4
    grid[pos] = (grid[pos] + 1) % 4
    infections += 1 if grid[pos] == 2 else 0
    pos = (pos[0] + directions[cur_dir][0], pos[1] + directions[cur_dir][1])

print("Second part:", infections)
