firewall = [(k, v) for (k, v) in (map(int, line.strip("\n").split(": ")) for line in open("inputs/13.in"))]

def scanner_pos(layer, time=0):
    pos = layer[0] + time
    height = layer[1]
    move = pos % (2 * (height - 1))

    return 2 * (height - 1) - move if move > height - 1 else move


first = sum([x[0] * x[1] if scanner_pos(x) == 0 else 0 for x in firewall])
print("First: {}".format(first))

# Second part
t = 0
all_clear = False if first != 0 else True

while not all_clear:
    t += 1
    severity = sum([1 if x[0] == scanner_pos(x, t) == 0 else x[0] * x[1] if scanner_pos(x, t) == 0 else 0 for x in firewall])
    all_clear = True if severity == 0 else False

print("Second: {}".format(t))
