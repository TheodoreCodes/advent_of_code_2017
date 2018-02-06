directions = ["n", "ne", "se", "s", "sw", "nw"]
steps = dict(zip(directions, [0] * 6))


max_steps = 0
def calc_steps():
    global max_steps
    total_steps = 0
    for _, i in steps.items():
        total_steps += i
    if total_steps > max_steps:
        max_steps = total_steps


def func(operator, value):
    index_expr = "(index {} {}) % 6"
    i = eval(index_expr.format(operator, value))
    d = directions[i]
    if int(value) > 1:
        if steps[d] > 0:
            steps[d] -= 1
            steps[cur_dir] -= 1 if steps[cur_dir] > 0 else 0
            if value == "2":
                key = directions[eval(index_expr.format(operator, "1"))]
                steps[key] += 1
            calc_steps()
        elif operator == "+":
            func("-", value)
        else:
            func("+", str(int(value) - 1))
    else:
        steps[cur_dir] += 1


for cur_dir in open("inputs/11.in").read().split(","):
    index = directions.index(cur_dir)
    func("+", "3")

calc_steps()

print(max_steps)