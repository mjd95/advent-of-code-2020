def is_valid(lower, upper, letter, password):
    lower = int(lower)
    upper = int(upper)
    return (password[lower-1] == letter) != (password[upper-1] == letter)

with open("input.txt") as f:
    lines = [line.strip() for line in f if line.strip()]

num_valid = 0
for line in lines:
    (policy, password) = line.split(':')
    (rnge, letter) = policy.split(' ')
    (lower, upper) = rnge.split('-')
    password = password.strip()

    # check valid
    if is_valid(lower, upper, letter, password): num_valid += 1

print(num_valid)



