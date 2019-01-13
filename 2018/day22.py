from collections import defaultdict
from copy import copy

grid = defaultdict(int)
for j, line in enumerate(open("inputs/22.in").readlines()):
    for i, v in enumerate(line.strip("\n")):
        grid[(i, j)] = 2 if v == '#' else 0

'''
0 - Clean
1 - Weakend
2 - Infected
3 - Flagged
'''
def contaminate(gap, bursts):
    local_grid = copy(grid)

    pos = (len(line) // 2, len(line) // 2)
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    cur_dir = 0
    infections = 0

    for _ in range(bursts):
        cur_dir = (cur_dir + local_grid[pos] - 1) % 4
        local_grid[pos] = (local_grid[pos] + gap) % 4
        infections += 1 if local_grid[pos] == 2 else 0
        pos = (pos[0] + directions[cur_dir][0], pos[1] + directions[cur_dir][1])

    return infections


print("First part:", contaminate(2, 10_000))
print("Second part:", contaminate(1, 10_000_000))
