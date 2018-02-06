circ_buf = [0]


def spin(spins, val):
    cur_pos = 0
    i = 1
    while i < spins:
        cur_pos = (cur_pos + 329) % i + 1
        circ_buf.insert(cur_pos, i)
        i += 1
    return circ_buf[(circ_buf.index(val) + 1) % len(circ_buf)]


def spin_2():
    cur_pos = 0
    i = 1
    val_to_return = 0
    while i < 50_000_000:
        cur_pos = (cur_pos + 329) % i + 1
        if cur_pos == 1:
            val_to_return = i
        i += 1
    return val_to_return


print("First part:", spin(2018, 2017))
print("Second part:", spin_2())
