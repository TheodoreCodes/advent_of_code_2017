particles = []
temp = []

def initialiaze(line, i, t):
    line = line.replace(">", ")\n").replace("<", "(").replace(", ", "")
    d = locals()
    exec(line)
    p, v, a = d['p'], d['v'], d['a']

    particles.append([p, v, a, i, sum([abs(a[i]*(t**2)/2 + v[i]*t + p[i]) for i in range(3)])])


def part_1():
    for index, line in enumerate(open("inputs/20.in").readlines()):
        initialiaze(line, index, 1000)

    return sorted(particles, key=lambda x: x[4])[0][3]


print("First part:", part_1())