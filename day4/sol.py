def is_valid(passport):
    ks = set(passport.keys())
    validkeys = 'byr' in ks and 'iyr' in ks and 'eyr' in ks and 'hgt' in ks and 'hcl' in ks and 'ecl' in ks and 'pid' in ks
    if not validkeys: return False

    if not (1920 <= int(passport['byr']) and int(passport['byr']) <= 2002): return False

    if not (2010 <= int(passport['iyr']) and int(passport['iyr']) <= 2020): return False

    if not (2020 <= int(passport['eyr']) and int(passport['eyr']) <= 2030): return False

    if 'cm' in passport['hgt']:
        h = int(passport['hgt'].replace('cm', ''))
        if not (150 <= h and h <= 193): return False
    elif 'in' in passport['hgt']:
        h = int(passport['hgt'].replace('in', ''))
        if not (59 <= h and h <= 76): return False
    else:
        return False

    if not passport['hcl'].startswith('#'): return False
    for c in passport['hcl'][1:]:
        if not (c.isnumeric() or c.islower()): return False

    if not passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']: return False

    if not (passport['pid'].isnumeric() and len(passport['pid']) == 9): return False

    return True

with open("input.txt") as f:
    lines = [line.strip() for line in f if line]

num_valid = 0
cur_passport = dict()
for line in lines:
    if line == "":
        if is_valid(cur_passport): num_valid += 1
        cur_passport = dict()
        continue

    for pair in line.split(' '):
        (k, v) = pair.split(':')
        cur_passport[k] = v

if is_valid(cur_passport): num_valid += 1

print(num_valid)