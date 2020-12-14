with open("input.txt") as f:
    lines = [line.strip() for line in f if line.strip()]

def set_with_bitmask(n, bitmask_sets, bitmask_clears):
    for i in bitmask_sets:
        n = n | (1<<i)
    for i in bitmask_clears:
        n = n & ~(1<<i)
    return n

def mem_bitmask(m, bitmask_sets, bitmask_floats):
    for i in bitmask_sets:
        m = m | (1<<i)
    ret = [m]
    for i in bitmask_floats:
        # emit the two possible numbers coming from both values of
        # ridiculously inefficient way to do this but doesn't matter
        k = 0
        orig_len = len(ret)
        while k < orig_len:
            ret.append(ret[k] | (1<<i))
            ret.append(ret[k] & ~(1<<i))
            k += 1
    return list(set(ret))

#mem = {}
#for line in lines:
#    (l, r) = line.split(' = ')
#    if l == "mask":
#        bitmask_sets = []
#        bitmask_clears = []
#        i = 0
#        while i < len(r):
#            if r[len(r)-i-1] == "1":
#                bitmask_sets.append(i)
#            elif r[len(r)-i-1] == "0":
#                bitmask_clears.append(i)
#            i += 1
#    else:
#        memloc = int(l.lstrip("mem[").rstrip("]"))
#        mem[memloc] = set_with_bitmask(int(r), bitmask_sets, bitmask_clears)
#
#tot = 0
#for (k, v) in mem.items():
#    tot += v
#print(tot)

mem = {}
for line in lines:
    (l, r) = line.split(' = ')
    if l == "mask":
        bitmask_sets = []
        bitmask_clears = []
        bitmask_floats = []
        i = 0
        while i < len(r):
            if r[len(r)-i-1] == "1":
                bitmask_sets.append(i)
            elif r[len(r)-i-1] == "X": 
                bitmask_floats.append(i)
            i += 1
    else:
        memloc = int(l.lstrip("mem[").rstrip("]"))
        to_set = mem_bitmask(memloc, bitmask_sets, bitmask_floats)
        for t in to_set:
            mem[t] = int(r)

tot = 0
for (k, v) in mem.items():
    tot += v
print(tot)
