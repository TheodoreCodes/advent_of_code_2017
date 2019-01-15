with open('inputs/5.in') as f:
    polymer = f.read()

def func(polymer):
    stack = [polymer[0]]
    for l in polymer[1:]:
        if (l.isupper() and l.lower() == stack[-1]) or (l.islower() and l.upper() == stack[-1]):
            stack.pop()
        else:
            stack.append(l)

    return stack


# Part 1
part_1 = func(polymer)
print(len(part_1))

# Part 2
part_1 = ''.join(part_1)
part_2 = min([len(func(part_1.replace(x.lower(), '').replace(x.upper(), ''))) for x in set(part_1.lower())])
print(part_2)

