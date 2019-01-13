INPUT = 265149

def part_1():
    temp = 1
    x = 0
    y = 0

    while (temp + 2) ** 2 < INPUT:
        temp += 2
        x += 1
        y -= 1

    oddSquare = temp ** 2
    steps = (temp + 1)
    difference = INPUT - oddSquare
    noOfCompleteSides = difference // steps

    if noOfCompleteSides == 3:
        y -= 1
        x = x - steps + 1 + (difference % steps)

    return abs(y) + abs(x)


def part_2():
    x = 1
    y = 0

    currentNum = 0
    spiral = {"0,0": 1}
    prevSide = 1
    sideLength = 0
    counter = 2
    direction = ['r', 'u', 'l', 'd']

    def get_number():
        nonlocal currentNum, spiral, x, y
        sum = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i != 0 or j != 0:
                    key = "{},{}".format(x + i, y + j)
                    if key in spiral:
                        sum += spiral[key]
        currentNum = sum
        return sum

    while currentNum <= INPUT:
        spiral["{},{}".format(x, y)] = get_number()

        if sideLength == 0:
            direction.append(direction.pop(0))
            counter -= 1
            if counter == 0:
                sideLength = prevSide + 1
                prevSide = sideLength
                counter = 2
            else:
                sideLength = prevSide

        if direction[0] == 'r':
            x += 1
        elif direction[0] == 'u':
            y += 1
        elif direction[0] == 'l':
            x -= 1
        elif direction[0] == 'd':
            y -= 1
        sideLength -= 1
    return currentNum


print("First part:", part_1())
print("Second part:", part_2())
