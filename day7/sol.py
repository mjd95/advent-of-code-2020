from collections import defaultdict

with open("input.txt") as f:
    lines = [line.strip() for line in f if line.strip()]

mapping = defaultdict(list)
nums = defaultdict(list)

for line in lines:
    (outter_str, inner_str) = line.split('contain')
    outter_bag_color = ' '.join(outter_str.split(' ')[:2])
    inners = inner_str.split(',')
    for inner in inners:
        inner_num = inner.split(' ')[1]
        inner_bag_color = ' '.join(inner.split(' ')[2:4])
        if inner_num == 'no': continue
        mapping[outter_bag_color].append(inner_bag_color)
        nums[outter_bag_color].append(inner_num)


memo = {}
def count(color, mapping, nums):
    if color in memo:
        return memo[color]

    children = mapping[color]
    children_nums = nums[color]
    if len(children) == 0:
        memo[color] = 1
        return 1

    to_return = 1
    for i in range(len(children)):
        to_return += int(children_nums[i]) * count(children[i], mapping, nums)

    memo[color] = to_return
    return to_return

print(count('shiny gold', mapping, nums)-1) 
print(memo)
