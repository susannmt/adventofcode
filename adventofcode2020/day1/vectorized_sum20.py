import numpy

expences = [int(e) for e in open("input.txt").readlines()]

ex = numpy.tile(numpy.array(expences), (len(expences), 1))
sums = ex + ex.transpose()

indexes = numpy.where(sums==2020)[0]
num1, num2 = expences[indexes[0]], expences[indexes[1]]
print(num1, num2, num1*num2)
