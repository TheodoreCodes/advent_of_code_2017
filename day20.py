from collections import defaultdict


particles = []
def initialiaze(line, i):
    line = line.replace(">", ")\n").replace("<", "(").replace(", ", "")
    d = locals()
    exec(line)
    p, v, a = d['p'], d['v'], d['a']

    particles.append([p, v, a, i])


for index, l in enumerate(open("inputs/20.in").readlines()):
    initialiaze(l, index)


def part_1():
    t = 1000
    return sorted(
        [(i, sum([abs(a[j] * (t ** 2) / 2 + v[j] * t + p[j]) for j in range(3)])) for (p, v, a, i) in particles],
        key=lambda x: x[1])[0][0]


def part_2():
    destroyed = 0
    for t in range(1000):
        collisions = defaultdict(list)
        for i, p in enumerate(particles):
            key = tuple([p[0][i] + t * p[1][i] + (t/2)*(t+1)*p[2][i] for i in range(3)])
            collisions[key].append(i)

        for c in collisions.values():
            if len(c) > 1:
                destroyed += len(c)

    return len(particles) - destroyed


print("First part:", part_1())
print("Second part", part_2())




# ALTERNATIVE WAY FOR PART 1
# counter = 0
# def order_changed(list1, list2):
#     global counter
#     for i in range(len(list1)):
#         if list1[i][0] != list2[i][0]:
#             counter = 0
#             return True
#     counter += 1
#     return False if counter > 1 else True

# def part_1():
#     t = 1000
#     current = sorted([(index, sum([abs(a[i]*(t**2)/2 + v[i] * t + p[i]) for i in range(3)])) for (p, v, a, index) in particles], key=lambda x: x[1])
#     previous = list(current)
#
#     while order_changed(previous, current) if t != 1 else True:
#         previous, current = list(current), sorted([(index, sum([abs(a[i]*(t**2)/2 + v[i]*t + p[i]) for i in range(3)])) for (p, v, a, index) in particles], key=lambda x: x[1])
#         t += 1
#     return current[0][0]
