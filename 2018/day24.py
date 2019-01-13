components = []
for l in open("inputs/24.in").readlines():
    components.append(tuple(map(int, l.strip("\n").split("/"))))

bridges = []

def make_bridges(last_port, bridge):
    for c in components:
        if last_port in c and c not in bridge:
            make_bridges(c[0] if last_port == c[1] else c[1], bridge[:] + [c])
    bridges.append(bridge)


make_bridges(0, [])
max_len = sorted(bridges, key=lambda b: (len(b), sum(map(sum, b))), reverse=True)[0]

print("First part:", max([sum(map(sum, b)) for b in bridges]))
print("Second part:", sum(map(sum, max_len)))
