import numpy

with open("input.txt", "r") as input_file:
    coordinates = [line.split(', ') for line in input_file.readlines()]
    coordinates = [[int(l[0]), int(l[1])] for l in coordinates]
xmax = max(coordinates, key=lambda x: x[0])[0]
ymax = max(coordinates, key=lambda x: x[1])[1]

area_matrix = numpy.zeros((xmax, ymax)) -1
dist_to_all = numpy.zeros((xmax, ymax))

for i in range(xmax):
    for j in range(ymax):
        distances = numpy.zeros(len(coordinates))
        for nr, coordinate in enumerate(coordinates):
            distances[nr] = abs(i-coordinate[0]) + abs(j-coordinate[1])

        if numpy.sum(distances == numpy.min(distances)) == 1:
            area_matrix[i, j] = numpy.argmin(distances)

        dist_to_all[i, j] = numpy.sum(distances)

outer = area_matrix.copy()
outer[1:-1, 1:-1] = -1
largest = 0
for nr in range(len(coordinates)):
    if nr in outer:
        continue
    largest = max(largest, (area_matrix == nr).sum())

print(largest)
print(numpy.sum(dist_to_all<10000))
