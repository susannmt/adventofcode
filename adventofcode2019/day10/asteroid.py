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
print(detected)
print(numpy.amax(detected))
