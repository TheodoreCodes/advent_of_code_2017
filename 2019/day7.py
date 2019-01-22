import re
from collections import defaultdict

tasks = set()
dependents = defaultdict(list)
with open('inputs/7.in') as f:
    for line in f:
        a, b = re.findall(r' [A-Z] ', line)
        tasks |= {a, b}
        dependents[b].append(a)

part_1 = []

for _ in tasks:
    part_1.append(min([x for x in tasks if x not in part_1 and set(part_1) >= set(dependents[x])]))

# Part 1
print(''.join(map(lambda s: s.replace(" ", ""), part_1)))

done = []
first_step = min([x for x in tasks if set(done) >= set(dependents[x])])
curr_task = [first_step] + ([None] * 4)

tasks.remove(first_step)

curr_task_start = [0] * 5
seconds = 0

while tasks or curr_task.count(None) != len(curr_task):
    for worker_id in range(5):
        if curr_task[worker_id] and (curr_task_start[worker_id] + (ord(curr_task[worker_id].replace(" ", "")) - 4) == seconds):
            done.append(curr_task[worker_id])
            curr_task[worker_id] = None

        candidates = [x for x in tasks if set(done) >= set(dependents[x])]

        if candidates and curr_task[worker_id] is None:
            step = min(candidates)
            tasks.remove(step)
            curr_task[worker_id] = step
            curr_task_start[worker_id] = seconds

    if tasks or curr_task.count(None) != len(curr_task):
        seconds += 1

# Part 2
print(seconds)

