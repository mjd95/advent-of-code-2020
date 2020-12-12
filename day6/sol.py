with open("input.txt") as f:
    lines = [line.strip() for line in f]

cur_seen = dict()
cur_group_size=0
total_count = 0
for line in lines:
    if line=="":
        cur_count = len([v for v in cur_seen.values() if v == cur_group_size])
        total_count += cur_count
        cur_group_size = 0
        cur_seen = dict()
        continue
    cur_group_size += 1
    for c in line:
        if c not in cur_seen:
            cur_seen[c] = 1
        else:
            cur_seen[c] += 1

cur_count = len([v for v in cur_seen.values() if v==cur_group_size])
total_count += cur_count

print(total_count)
