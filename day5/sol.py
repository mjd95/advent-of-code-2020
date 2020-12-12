def get_id(line):
    i = 0
    row_num = 0
    two_power = 6
    while i < 7:
        if line[i] == 'B': row_num += 2**two_power
        two_power -= 1
        i += 1
    seat_num = 0
    two_power = 2
    while i < 10:
        if line[i] == 'R': seat_num += 2**two_power
        two_power -= 1
        i += 1
    return row_num * 8 + seat_num

with open("input.txt") as f:
    lines = [line.strip() for line in f if line.strip()]

seen = set()
for line in lines:
    seen.add(get_id(line))

print(set(range(59, 905)) - seen)
