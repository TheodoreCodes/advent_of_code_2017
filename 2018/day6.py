snapshot_list = []
counter = 0

with open('inputs/6.in') as f:
    currentState = list(map(int, f.readline().split()))
    f.close()


def compare_snapshots():
    snapshot = ",".join(str(x) for x in currentState)
    for i in snapshot_list:
        if i == snapshot:
            return True
    snapshot_list.append(snapshot)
    return False


def update_state():
    global counter
    max_val = 0
    max_pos = 0
    for i in range(len(currentState)):
        if max_val < currentState[i]:
            max_val = currentState[i]
            max_pos = i

    currentState[max_pos] = 0
    i = max_pos
    while max_val > 0:
        if i == len(currentState) - 1:
            i = 0
        else:
            i += 1
        currentState[i] += 1
        max_val -= 1


while not compare_snapshots():
    update_state()

j = snapshot_list.index(",".join(str(l) for l in currentState))

print(len(snapshot_list) - j)
