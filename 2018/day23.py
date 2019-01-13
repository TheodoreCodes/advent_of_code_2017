import string
import re

def process_instruction(line):
    ins = re.search('([a-z]{3}) ([a-z0-9]) (-?[a-z0-9]+)?', line)
    return [ins.group(1), ins.group(2), ins.group(3)]


registers = {x: 0 for x in string.ascii_lowercase[:8]}
instructions = [process_instruction(l) for l in open("inputs/23.in").readlines()]

i = 0
def execute(ins):
    global i
    command, x, y = instructions[ins]
    y = registers[y] if y.islower() else int(y)
    i += 1
    if command == 'set':
        registers[x] = y
    elif command == 'sub':
        registers[x] -= y
    elif command == 'mul':
        registers[x] *= y
    elif command == 'jnz':
        x = registers[x] if x.islower() else int(x)
        i += y - 1 if x != 0 else 0


muls = 0

while i < len(instructions):
    muls += 1 if instructions[i][0] == 'mul' else 0
    execute(i)

print("First part", muls)

reg_h = 0
for i in range(105_700, 105_700 + 17_001, 17):
    for j in range(2, i):
        if i % j == 0:
            reg_h += 1
            break

print("Second part:", reg_h)
