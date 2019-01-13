stream = iter(open("inputs/9.in", "r").read())
group_level = 1
inside_garbage = False
total = 0

garbage_count = 0

for char in stream:
    if char == "!":
        stream.__next__()
        continue
    else:
        if inside_garbage:
            if char == ">":
                inside_garbage = False
            else:
                garbage_count += 1
        else:
            if char == "<":
                inside_garbage = True
            elif char == "{":
                total += group_level
                group_level += 1
                print(total)
            elif char == "}":
                group_level -= 1

print(total)

print(garbage_count)