import numpy
import matplotlib.pyplot as plt

with open("input.txt", "r") as input_file:
    points = input_file.readlines()

n = len(points)
x = numpy.zeros(n)
y = numpy.zeros(n)
vx = numpy.zeros(n)
vy = numpy.zeros(n)

for i in range(n):
    x[i] = int(points[i][10:16])
    y[i] = int(points[i][18:24])
    vx[i] = int(points[i][-8:-6])
    vy[i] = int(points[i][-4:-2])

for second in range(10305, 10320):
    plt.scatter(y+second*vy, x+second*vx)
    plt.savefig("sec{num:04d}".format(num=second))
    plt.clf()
