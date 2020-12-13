with open("input.txt") as f:
    ratings = [int(line.strip()) for line in f if line.strip()]

ratings = [0] + sorted(ratings)
print(ratings)

# count differences
one_diffs = 0
three_diffs = 0
for i in range(1, len(ratings)):
    if ratings[i]-ratings[i-1] == 1:
        one_diffs += 1
    elif ratings[i]-ratings[i-1] == 3:
        three_diffs += 1

three_diffs += 1

print(one_diffs, three_diffs, one_diffs*three_diffs)
 
memo = {len(ratings)-1: 1}
def number_valid_from(i, ratings):
    if i in memo:
        return memo[i]
    
    to_ret = 0
    for j in range(i+1, min(i+4, len(ratings))):
        if ratings[j]-ratings[i]<=3:
            to_ret += number_valid_from(j, ratings)
    
    memo[i] = to_ret
    return memo[i]

print(number_valid_from(0, ratings))