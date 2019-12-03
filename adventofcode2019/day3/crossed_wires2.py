import numpy

wire1, wire2 = [line.split(',') for line in open("input.txt").readlines()]

grid1 = numpy.zeros((20000, 20000))

i, j = 5000, 5000
count = 1
for step in wire1:
    direction = step[0]
    length = int(step[1:])
    for steps in range(1, length+1):
        if direction == "R":
            j += 1
        if direction == "L":
            j -= 1
        if direction == "U":
            i += 1
        if direction == "D":
            i -= 1
        if grid1[i][j] == 0:
            grid1[i][j] = count
        count += 1

grid2 = numpy.zeros((20000, 20000))
i, j = 5000, 5000
count = 1

for step in wire2:
    direction = step[0]
    length = int(step[1:])
    for steps in range(length):
        if direction == "R":
            j += 1
        if direction == "L":
            j -= 1
        if direction == "U":
            i += 1
        if direction == "D":
            i -= 1
        if grid2[i][j] == 0:
            grid2[i][j] = count
        count += 1


crossed_grid = ((grid1 > 0).astype(int) + (grid2 > 0).astype(int)) > 1

total_steps = []
for i in range(20000):
    for j in range(20000):
        if crossed_grid[i][j]:
            total_steps.append(grid1[i][j] + grid2[i][j])

print(min(total_steps))
