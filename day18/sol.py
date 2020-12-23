with open("input.txt") as f:
    lines = [line.strip().replace(" ", "") for line in f if line.strip()]


def process_line(line):
    if len(line)==0:
        return 0

    accs = [None]
    ops = ['']
    nest_level = 0
    i = 0
    while i < len(line):
        if line[i] == '+':
            ops[nest_level] = '+'
            i += 1
        elif line[i] == '*':
            ops[nest_level] = '*'
            i += 1
        elif line[i].isnumeric():
            if ops[nest_level] == '+':
                accs[nest_level] += int(line[i])
                ops[nest_level] = ''
            elif ops[nest_level] == '*':
                accs[nest_level] *= int(line[i])
                ops[nest_level] = ''
            else:
                accs[nest_level] = int(line[i])
            i += 1
        elif line[i] == '(':
            accs.append(None)
            ops.append('')
            nest_level += 1
            i += 1
        elif line[i] == ')':
            final = accs.pop()
            nest_level -= 1
            if ops[nest_level] == '+':
                accs[nest_level] += final
                ops[nest_level] = ''
            elif ops[nest_level] == '*':
                accs[nest_level] *= final
                ops[nest_level] = ''
            else:
                accs[nest_level] = final
            i += 1
        
    return accs[0]

#tot = 0
#for line in lines:
#    tot += process_line(line)
#

def process_flat_line(line):
    # evaluate pluses, left-to-right
    while '+' in line:
        first_plus = line.index('+')
        sub = int(line[first_plus-1]) + int(line[first_plus+1])
        line[first_plus-1:first_plus+2] = [sub]
    
    while '*' in line:
        first_mult = line.index('*')
        sub = int(line[first_mult-1]) * int(line[first_mult+1])
        line[first_mult-1:first_mult+2] = [sub]

    return int(line[0])


# for part 2, first flatten all brackets
def process_line2(line):
    if '(' not in line:
        # can process directly
        return process_flat_line(line)

    # remove the first open-close bracket we can
    start = line.index('(')
    end = start + 1
    while end < len(line):
        if line[end] == ')':
            # we're good
            break
        elif line[end] == '(':
            # need to re-evaluate the situation
            start = end
        end += 1
    sub = process_flat_line(line[start+1:end])
    line[start:end+1] = [sub]
    return process_line2(line)



tot = 0
for line in lines:
    tot += process_line2(list(line))

print(tot)
