import re
from collections import Counter


def part_1():
    holders_list = []
    held_list = []

    for x in open("inputs/7.in").readlines():
        line = re.search("(.*) \((.*)\)( -> )?(.*)?", x)
        if line.group(1):
            holders_list.append(line.group(1))
        if line.group(4):
            held_list.extend(line.group(4).split(", "))

    return set(holders_list).difference(held_list).pop()


ROOT = part_1()

tree = {}

# Build the tree
for x in open("inputs/7.in").readlines():
    line = re.search("(.*) \((.*)\)( -> )?(.*)?", x)
    temp = {}
    if line.group(2):
        temp['weight'] = line.group(2)
    if line.group(4):
        temp['children'] = line.group(4).split(", ")
    else:
        temp['children'] = []

    tree[line.group(1)] = temp


def get_weight(subroot):
    total = int(tree[subroot]["weight"])
    for c in tree[subroot]['children']:
        total += get_weight(c)
    return total


def get_children_weight(subroot):
    weights = []
    for c in tree[subroot]['children']:
        weights.append(get_weight(c))
    return weights


def is_balanced(root):
    if not tree[root]['children']:
        return True
    children_weights = get_children_weight(root)

    return len(set(children_weights)) == 1


answer = ROOT
weight_difference = 0


def find_unbalanced(root):
    global answer, weight_difference

    def flatten():
        balanced = weights.index((max(counter, key=counter.get)))
        return weights[balanced] - weights[unbalanced]

    if not is_balanced(root):
        weights = get_children_weight(root)
        counter = Counter(weights)
        unbalanced = weights.index((min(counter, key=counter.get)))
        if root == ROOT:
            weight_difference = flatten()
        answer = tree[root]["children"][unbalanced]
        find_unbalanced(answer)
    else:
        ans_weight = int(tree[answer]["weight"])
        print("Node: " + answer)
        print("Default weight: " + str(ans_weight))
        print("Correct weight: " + str(ans_weight + weight_difference))


print("First part:", ROOT)
find_unbalanced(ROOT)
