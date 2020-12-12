with open("input.txt") as f:
    grid = [line.strip() for line in f if line.strip()]
    

total = 1
for (ishift, jshift) in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    i=0
    j=0
    count=0
    
    while(j<len(grid)):
        if grid[j][i%len(grid[j])]=='#':
            count += 1
        i += ishift
        j += jshift 
    
    total *= count

print(total)
