inputs = dict()
parsed = dict()
for line in open("inputs/12.in").readlines():
    item = line.strip("\n").split(" <-> ")
    key = int(item[0])
    inputs[key] = [int(x) for x in item[1].split(", ")]
    parsed[key] = 0

parsed[0] = 1
counter = 1

def func(pid):
    global counter
    if None not in inputs[pid]:
        for id in inputs[pid]:
            if id != pid and parsed[id] == 0:
                counter += 1
                inputs[pid][inputs[pid].index(id)] = None
                parsed[id] += 1
                func(id)


# First part
func(0)
print(counter)

# Second part
groups = 1
for k, v in parsed.items():
    if v == 0:
        func(k)
        groups += 1
print(groups)
