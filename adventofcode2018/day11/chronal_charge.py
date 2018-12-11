import numpy

grid_serial_number = 6303
grid = numpy.zeros((300, 300))

for y in range(1,301):
    for x in range(1,301):
        rack_ID = x+10
        power_level = rack_ID*y
        power_level += grid_serial_number
        power_level *= rack_ID
        digit = str(power_level).rjust(3, '0')[-3]
        power_level = int(digit) - 5
        grid[y-1, x-1] = power_level

def find_best(grid_size):
    best_power = 0
    best_grid = None
    best_grid_size = 0
    for n in grid_size:
        sums = numpy.zeros((300, 300))
        for y in range(300-n):
            for x in range(300-n):
                square = grid[y:y+n, x:x+n]
                sums[y, x] = numpy.sum(square)

        best_y, best_x = numpy.unravel_index(numpy.argmax(sums, axis=None), sums.shape)
        if sums[best_y, best_x] > best_power:
            best_grid = (best_x+1, best_y+1)
            best_power = sums[best_y, best_x]
            best_grid_size = n
    return best_grid, best_grid_size

print(find_best([3]))
print(find_best(range(300)))

