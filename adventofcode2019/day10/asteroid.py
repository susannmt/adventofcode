import numpy
import math

space = [list(row.strip()) for row in open("input.txt").readlines()]
width = len(space)
hight = len(space[0])
detected = numpy.zeros((width, hight))

for i in range(width):
    for j in range(hight):
        if space[i][j] == "#":
            angles = set()
            for m in range(width):
                for n in range(hight):
                    if space[m][n] == ".":
                        continue
                    if i == m and j == n:
                        continue
                    a = i-m
                    b = j-n
                    angles.add(math.atan2(b,a))

            detected[i][j] = len(angles)

asteroids = numpy.amax(detected)
print(asteroids)

position = numpy.argwhere(detected == asteroids)

asteroid_map = {}
for m in range(width):
    for n in range(hight):

        if space[m][n] == ".":
            continue
        if position[0][0] == m and position[0][1] == n:
            continue
        a = position[0][0]-m
        b = position[0][1]-n
        distance = a+b
        angle = math.atan2(b,a)
        if angle not in asteroid_map:
            asteroid_map[angle] = []
        asteroid_map[angle].append([m,n, distance])


degree = sorted(asteroid_map.keys())[::-1]
i = degree.index(0.0)
blasted = []
for t in range(int(asteroids)):
    if i >= len(degree):
        i -= len(degree)
    if not asteroid_map[degree[i]]:
        continue
    distances = numpy.array([target[-1] for target in asteroid_map[degree[i]]])
    remove_index = numpy.argmin(distances)
    blast = asteroid_map[degree[i]].pop(remove_index)
    blasted.append(blast)
    i += 1

print(blasted[199][1]*100+blasted[199][0])
