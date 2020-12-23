with open("input.txt") as f:
    lines = [line.strip() for line in f if line.strip()]


# work out size of thing needed for 6 iterations
num_iterations = 6


x_len = num_iterations + len(lines[0]) + num_iterations
y_len = num_iterations + len(lines) + num_iterations 
z_len = num_iterations + 1 + num_iterations
w_len = num_iterations + 1 + num_iterations

grid = [[[['.' for x in range(x_len)] for y in range(y_len)] for z in range(z_len)] for w in range(w_len)]


def neighbours(x, y, z, w):
    to_ret = []
    for w1 in range(-1, 2):
        for z1 in range(-1, 2):
            for y1 in range(-1, 2):
                for x1 in range(-1, 2):
                    if (x1, y1, z1, w1) == (0, 0, 0, 0):
                        continue
                    if in_bounds(x+x1, y+y1, z+z1, w+w1):
                        to_ret.append((x+x1, y+y1, z+z1, w+w1))
    return to_ret


def in_bounds(x, y, z, w):
    if x < 0 or x >= x_len:
        return False
    if y < 0 or y >= y_len:
        return False
    if z < 0 or z >= z_len:
        return False
    if w < 0 or w >= w_len:
        return False

    return True


def evolve(grid):
    to_active = []
    to_inactive = []
    for w in range(0, w_len):
        for z in range(0, z_len):
            for y in range(0, y_len):
                for x in range(0, x_len):
                    active_nbrs = 0
                    for nbr in neighbours(x, y, z, w):
                        if grid[nbr[3]][nbr[2]][nbr[1]][nbr[0]] == '#':
                            active_nbrs += 1
                    if grid[w][z][y][x] == '#':
                        if active_nbrs != 2 and active_nbrs != 3:
                            to_inactive.append([x, y, z, w])
                    else:
                        if active_nbrs == 3:
                            to_active.append([x, y, z, w])
    for t in to_active:
        (x, y, z, w) = t
        grid[w][z][y][x] = '#'
    for t in to_inactive:
        (x, y, z, w) = t
        grid[w][z][y][x] = '.'

def print_grid(z):
    for y in range(0, y_len):
        l = ""
        for x in range(0, x_len):
            l += grid[z][y][x]
        print(l)


# fill out initial grid
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == '#':
            grid[num_iterations][num_iterations][num_iterations+y][num_iterations+x] = '#'        

#print("n=0, z=0")
#print_grid(num_iterations)

for i in range(num_iterations):
    print(i)
    evolve(grid)

#print("n=1, z=-1")
#print_grid(num_iterations-1)
#print("n=1, z=0")
#print_grid(num_iterations)
#print("n=1, z=1")
#print_grid(num_iterations+1)

tot_active = 0
for w in range(w_len):
    for z in range(z_len):
        for y in range(y_len):
            for x in range(x_len):
                if grid[w][z][y][x] == '#':
                    tot_active += 1

print(tot_active)
