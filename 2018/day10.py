lengths_1 = open("inputs/10.in").read().split(",")
lengths_1 = list(map(int, lengths_1))


def reverse_list(current_length, current_pos, num_list):
    if current_length < 256:
        start = current_pos
        end = (current_pos + current_length - 1) % 256
        num_of_changes = current_length // 2
        while num_of_changes != 0:
            temp = num_list[start]
            num_list[start] = num_list[end]
            num_list[end] = temp

            start += 1
            if start > 255:
                start = 0
            end -= 1
            if end < 0:
                end = 255
            num_of_changes -= 1


def solve(repeat, length):
    numbers = [x for x in range(256)]
    current_pos = 0
    skip_size = 0
    for _ in range(repeat):
        for l in length:
            reverse_list(l, current_pos, numbers)
            current_pos += l + skip_size
            current_pos %= 256
            skip_size += 1
    return numbers


first = solve(1, lengths_1)
# print("First part:", first[0] * first[1])


# Second part
def dense_hash(start, end, num_list):
    for i in range(start + 1, end + 1):
        num_list[start] ^= num_list[i]
    num_list[start + 1:end + 1] = []
    if end < len(num_list):
        dense_hash(start + 1, end + 1, num_list)


lengths_2 = [ord(c) for c in open("inputs/10.in").read()]
lengths_2.extend([17, 31, 73, 47, 23])

second = solve(64, lengths_2)
dense_hash(0, 15, second)
second = [hex(x)[2:].zfill(2) for x in second]

# print("Second part:", "".join(second))
