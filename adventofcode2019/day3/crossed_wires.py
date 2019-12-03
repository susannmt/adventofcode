import numpy

wire1, wire2 = [line.split(',') for line in open("input.txt").readlines()]

grid1 = numpy.zeros((20000, 20000))

i, j = 5000, 5000
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
        grid1[i][j] += 1

grid1 = (grid1 > 0).astype(int)
grid2 = numpy.zeros((20000, 20000))
i, j = 5000, 5000
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
        grid2[i][j] += 1

grid2 = (grid2 > 0).astype(int)

crossed_grid = grid1 + grid2 > 1

manhattan = []
for i in range(20000):
    for j in range(20000):
        if crossed_grid[i][j]:
            manhattan.append(abs(i-5000)+abs(j-5000))

print(min(manhattan))
