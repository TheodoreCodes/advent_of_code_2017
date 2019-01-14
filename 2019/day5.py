from collections import defaultdict

with open('inputs/5.in') as f:
    polymer = f.read()


i = 0
initial_length = j = len(polymer) - 1
units = defaultdict(lambda: 0)
while i < j:
    if abs(ord(polymer[i]) - ord(polymer[i+1])) == 32:
        polymer = polymer[:i] + polymer[(i+2):]
        units[polymer[i].lower()] += 2
        i -= 1
        j -= 2
    else:
        i += 1

# Part 1
print(len(polymer))