with open("input.txt") as f:
    lines = [int(line.strip()) for line in f if line.strip()]

preamble_length = 25

# compute the valid numbers from the preamble
i = preamble_length
while i < len(lines):
    valid_sums = []
    for j in range(i-preamble_length, i):
        for k in range(i-preamble_length, j):
            valid_sums.append(lines[j] + lines[k])
    if lines[i] not in valid_sums:
        target = lines[i]
        break
    i += 1

# find a contigous range that adds up to target
for window_size in range(2, len(lines)):
    for i in range(len(lines)-window_size):
        s = sum(lines[i:i+window_size])
        if s == target:
            print(max(lines[i:i+window_size]) + min(lines[i:i+window_size]))