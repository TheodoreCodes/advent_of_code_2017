import re

with open('inputs/6.in') as f:
    points = [tuple(map(int, re.findall(r'\d+', line))) for line in list(f)]

x_min, y_min = (min([x for x, y in points]), min([y for x, y in points]))
x_max, y_max = (max([x for x, y in points]), max([y for x, y in points]))

part_1 = [0 for x in range(len(points))]

def dist(p1, p2):
    return abs((p1[0] - p2[0])) + abs((p1[1] - p2[1]))

def get_closest_point(location):
    min_dist = dist((x_max, y_max), (x_min, y_min))
    index = 0

    for i, p in enumerate(points):
        distance = dist(p, location)
        if distance == min_dist:
            return None
        elif distance < min_dist:
            index = i
            min_dist = distance

    part_1[index] += 1


def check_distance(location):
    total = 0
    for p in points:
        total += dist(p, location)

    return 1 if total < 10000 else 0


part_2 = 0
for x in range(x_min, x_max):
        for y in range(y_min, y_max):
            get_closest_point((x, y))
            part_2 += check_distance((x, y))

# Part 1
print(max(part_1))
# Part 2
print(part_2)
