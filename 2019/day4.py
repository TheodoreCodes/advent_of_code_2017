import datetime
import re

with open('inputs/4.in') as f:
    log = list()
    for line in f:
        results = re.match("\[[0-9]{4}-(.*)\] (.*)", line)
        entry = dict()
        entry['time'] = results.group(1)
        entry['action'] = results.group(2)

        action = results.group(2)
        entry['guard_id'] = int(re.search(r'\d+', action).group()) if re.search(r'\d+', action) else None
        log.append(entry)

log.sort(key=lambda x: datetime.datetime.strptime(x['time'], '%m-%d %H:%M'))

asleep = dict()
guard_id = None
start_sleep = None

for l in log:
    minute = int(l['time'].split(':')[1])
    if l['guard_id'] is not None:
        guard_id = l['guard_id'] if l['guard_id'] is not None else guard_id
    elif "asleep" in l['action']:
        start_sleep = minute
    elif "wakes" in l['action']:
        asleep.setdefault(guard_id, [0]*59)
        for i in range(start_sleep, minute - 1):
            asleep[guard_id][i] += 1

# Part 1
asleep_copy = sorted(asleep.items(), key=lambda x: sum(x[1]), reverse=True)[0]
print(asleep_copy[0] * max([i for i, j in enumerate(asleep_copy[1]) if j == max(asleep_copy[1])]))


# Part 2
asleep_copy = sorted(asleep.items(), key=lambda x: max(x[1]), reverse=True)[0]
print(asleep_copy[0] * max([i for i, j in enumerate(asleep_copy[1]) if j == max(asleep_copy[1])]))
