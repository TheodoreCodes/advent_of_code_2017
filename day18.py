import re
from collections import defaultdict

last_played = ''
registers = defaultdict(int)
i = 0

def execute(ins):
    global last_played, i
    ins = re.search('([a-z]{3}) ([a-z]) ?(-?[a-z0-9]+)?', ins)
    command = ins.group(1)
    reg = ins.group(2)

    if command == 'snd':
        last_played = registers[reg]
    elif command == 'rcv' and registers[reg] > 0:
            return last_played
    else:
        val = registers[ins.group(3)] if ins.group(3).islower() else int(ins.group(3))
        if command == 'set':
            registers[reg] = val
        elif command == 'add':
            registers[reg] += val
        elif command == 'mul':
            registers[reg] *= val
        elif command == 'mod':
            registers[reg] %= val
        elif command == 'jgz':
            if registers[reg] > 0:
                i += val

    if command != 'jgz' or registers[reg] == 0:
        i += 1


def part_1():
    global i
    INPUT = open("inputs/18.in").readlines()
    while i < len(INPUT):
        to_return = execute(INPUT[i])
        if to_return:
            break
    return to_return


print("First part:", part_1())
