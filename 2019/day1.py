with open('inputs/1.in') as f:
    freq_changes = [x.strip() for x in f.readlines()]

def part_1():
    return sum(map(int, freq_changes))

def part_2():
    curr_freq = 0
    seen = {curr_freq}

    while True:
        for x in freq_changes:
            curr_freq += int(x)
            if curr_freq in seen:
                return curr_freq
            seen.add(curr_freq)


if __name__ == '__main__':
    print(part_1())
    print(part_2())
