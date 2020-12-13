with open("input.txt") as f:
    lines = [line.strip() for line in f if line.strip()]

x, y = 0, 0
wx, wy = 10, 1 # this should really be called offset or something
drs = [[1,0], [0, -1], [-1, 0], [0, 1]]
dr_pos = 0
for line in lines:
    op, arg = line[:1], int(line[1:])
    if op=='N':
        wy += arg
    elif op == 'E':
        wx += arg
    elif op == 'S':
        wy -= arg
    elif op == 'W':
        wx -= arg
    elif op == 'F':
        for i in range(arg):
            # move ship to waypoint
            x += wx
            y += wy
    elif op == 'L':
        num_turns = arg//90
        for i in range(num_turns):
            (wx, wy) = (-wy, wx)
    elif op == 'R':
        num_turns = arg//90
        for i in range(num_turns):
            (wx, wy) = (wy, -wx)

print(abs(x) + abs(y))

# some rotations
# 'R' (i.e clockwise). (1, 2) -> (2, -1) -> (-1, -2) -> (-2, 1). this is (wx, wy) -> (wy, -wx)