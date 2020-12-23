from collections import defaultdict

with open("input.txt") as f:
    # parse the rules
    rules = {}
    while True:
        line = f.readline().strip()
        if line.strip() == "":
            break
        
        (name, ranges) = line.split(": ")
        (r1, r2) = ranges.split(" or ")
        (r1_lower, r1_upper) = r1.split("-")
        (r2_lower, r2_upper) = r2.split("-")
        rules[name] = (int(r1_lower), int(r1_upper), int(r2_lower), int(r2_upper))

    line = f.readline().strip()
    if line != "your ticket:":
        print("broken")
        
    line = f.readline().strip()
    my_ticket = [int(n) for n in line.split(",")]

    line = f.readline().strip()

    line = f.readline().strip()
    if line != "nearby tickets:":
        print("broken")

    nearby_tickets = []
    while True:
        line = f.readline().strip()
        if line == "":
            break

        nearby_tickets.append([int(n) for n in line.split(",")])

print("rules:", rules)
print("other tickets:", nearby_tickets)

invalids = []
i = 0
l = len(nearby_tickets)
while i < l:
    # go through the numbers in this ticket and remove ones that are valid for no rules
    for n in nearby_tickets[i]:
        is_valid = False
        for rule_ranges in rules.values():
            (l1, u1, l2, u2) = rule_ranges
            if (l1 <= n and n <= u1) or (l2 <= n and n <= u2):
                is_valid = True
                break
        if not is_valid:
            del nearby_tickets[i]
            l -= 1
            break
    i += 1
print("valid other tickets:", nearby_tickets)

all_valid_tickets = nearby_tickets + [my_ticket]
print("all valid tickets:", all_valid_tickets)

possible_fields = [set() for _ in my_ticket]

for ticket in nearby_tickets:
    for idx, num in enumerate(ticket):
        fields = set()
        for name, v in rules.items():
            (l1, u1, l2, u2) = v
            if l1 <= num <= u1 or l2 <= num <= u2:
                fields.add(name)
        if fields:
            possible_fields[idx] = possible_fields[idx].intersection(fields) if possible_fields[idx] else fields
sorted_possible_fields = [
    [len(fields), idx, fields] for idx, fields in enumerate(possible_fields)
]
sorted_possible_fields.sort()
print(sorted_possible_fields)

visited = set()
to_ret = 1
for idx, data in enumerate(sorted_possible_fields):
    length, idx, fields = data

    field_name = list(fields - visited)[0]
    if 'departure' in field_name:
        to_ret *= my_ticket[idx]
    visited = visited.union(fields)
print(to_ret)