input = open('inputs/1.in').read()

sum = 0
HALFWAY = int(len(input) / 2)
for i in range(len(input)):
    if input[i] == input[int((i + HALFWAY) % len(input))]:
        sum += int(input[i])
print(sum)