import re
import sys
from collections import defaultdict

registers = defaultdict(int)
max_ever = -sys.maxsize
for x in open("inputs/8.in").readlines():
    #                  1         2         3              4       5         6
    line = re.search("(\w+)\s(inc|dec)\s([\-0-9]+)\sif\s(\w+)\s([!=<>]+)\s(.*)", x)
    expression = str(registers[line.group(4)]) + line.group(5) + line.group(6)
    if eval(expression):
        if line.group(2) == "inc":
            registers[line.group(1)] += int(line.group(3))
        elif line.group(2) == "dec":
            registers[line.group(1)] -= int(line.group(3))
        if max(registers.values()) > max_ever:
            max_ever = max(registers.values())

print(max(registers.values()))
print(max_ever)
