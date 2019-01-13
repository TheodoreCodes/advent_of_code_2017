from collections import defaultdict

STATES = {
    'A': [
        [1, 1, 'B'],
        [0, -1, 'C']
    ],
    'B': [
        [1, -1, 'A'],
        [1, 1, 'D']
    ],
    'C': [
        [1, 1, 'A'],
        [0, -1, 'E']
    ],
    'D': [
        [1, 1, 'A'],
        [0, 1, 'B']
    ],
    'E': [
        [1, -1, 'F'],
        [1, -1, 'C']
    ],
    'F': [
        [1, 1, 'D'],
        [1, 1, 'A']
    ]
}
cur_state = STATES['A']
cur_pos = 0
tape = defaultdict(int)

for _ in range(12919244):
    val = tape[cur_pos]
    tape[cur_pos] = cur_state[val][0]
    cur_pos += cur_state[val][1]
    cur_state = STATES[cur_state[val][2]]

print("Diagnostic checksum:",  sum(tape.values()))
