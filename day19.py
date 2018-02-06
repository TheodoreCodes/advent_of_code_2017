road = {(x, y): v for y, line in enumerate(open("inputs/19.in").read().splitlines()) for x, v in enumerate(line) if v != ' '}

DELTAS = (0, 1), (-1, 0), (0, -1), (1, 0)
cur_pos = next(iter(road))
direction = 0
positions = "|-"
letters = []
steps = 0
while len(road):
    if cur_pos in road:
        elem = road.pop(cur_pos)
        if elem == "+":
            for k, d in enumerate(DELTAS):
                neighbour = tuple(map(sum, zip(cur_pos, d)))
                if neighbour in road:
                    if road[neighbour] == positions[k % 2]:
                        direction = k
                        break
        elif elem.isalpha():
            letters.append(elem)

    cur_pos = tuple(map(sum, zip(cur_pos, DELTAS[direction])))
    steps += 1


print("First part", "".join(letters))
print("Seconds part", steps)