with open("input.txt") as f:
    lines = [line.strip() for line in f if line.strip()]

earliest_timestamp = int(lines[0])
ids = [int(n) for n in lines[1].split(',') if n != 'x']

print(earliest_timestamp)
print(ids)

smallest_above = earliest_timestamp * earliest_timestamp # something way big
chosen_bus = None
for n in ids:
    # find the least multiple of n which is larger than earliest timestamp
    if earliest_timestamp % n == 0:
        # exact match
        smallest_above = earliest_timestamp
        chosen_bus = n
        break

    t = n*(earliest_timestamp // n) + n
    if t < smallest_above:
        smallest_above = t
        chosen_bus = n

print((smallest_above-earliest_timestamp) * chosen_bus)

# for part 2 looking for number n which satisfies a bunch of congruence conditions
spl = lines[1].split(',')
remainders = [i for i in range(len(spl)) if spl[i] !='x']
print(ids)
print(remainders)

# we're looking for some number x with the property that (x+remainders[j])%ids[j] == 0 for each j
# use sieving
# ids[0], 2*ids[0], 3*ids[0], .... <- clearly they all satisfies x%ids[0]==0, find one that also satisfies x%ids[1]==-remainders[1]
# given that x, look at x+ids[0]*ids[1]*ids[2], x+2*ids[0]*ids[1]*ids[2], x+3*ids[0]*ids[1]*ids[2], ... <- clearly all work mod ids[0] and ids[1], find one that works mod ids[2]
# and so on
cur_mod = ids[0]
cur_sol = 0
for j in range(1, len(ids)):
    # find some value of cur_rem that satisfies the congruence with nxt_mod
    nxt_mod = cur_mod * ids[j]
    m = 0
    while True:
        if (cur_sol + m*cur_mod + remainders[j])%ids[j] == 0:
            cur_sol = cur_sol + m*cur_mod
            cur_mod = nxt_mod
            break
        m += 1
print(cur_sol)


