with open ("input.txt") as f:
    grid = [list(line.strip()) for line in f if line.strip()]

def print_grid(grid):
    for j in range(len(grid)):
        print(''.join(grid[j]))
    print('\n')

def in_bounds(i, j, grid):
    return i>=0 and i<len(grid[0]) and j>=0 and j<len(grid)

def num_occupied_neighbours(i, j, grid):
    dirs = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    num_occupied = 0
    for d in dirs:
        l = 1
        occupied = False
        while True:
            i1 = i + l*d[0]
            j1 = j + l*d[1]
            if not in_bounds(i1, j1, grid):
                break
            if grid[j1][i1] == '#':
                occupied = True
                break
            elif grid[j1][i1] == 'L':
                break
            l += 1
        if occupied:
            num_occupied +=1
    return num_occupied

num_occupied = 0
while True:
#    print_grid(grid)
    prv_occupied = num_occupied
    should_occupy= []
    should_vacate = []
    for j in range(0, len(grid)):
        for i in range(0, len(grid[0])):
            if grid[j][i] == 'L':
                if num_occupied_neighbours(i, j, grid) == 0:
                    should_occupy.append((i, j))
            if grid[j][i] == '#':
                if num_occupied_neighbours(i, j, grid) >= 5:
                    should_vacate.append((i, j))

    for (i, j) in should_occupy:
        grid[j][i] = '#'
    for (i, j) in should_vacate:
        grid[j][i] = 'L'

    num_occupied = 0
    for j in range(0, len(grid)):
        for i in range(0, len(grid[0])):
            if grid[j][i] == '#':
                num_occupied += 1

    print(num_occupied)
    if num_occupied == prv_occupied:
        break
