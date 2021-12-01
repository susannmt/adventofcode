import numpy

# part 1
with open("input.txt") as infile:
    data = infile.readlines()

increases = 0
for i in range(1, len(data)):
    if int(data[i]) > int(data[i-1]):
        increases += 1

print(increases)

# part 2 using arrays
array =  numpy.array(data, dtype=int)
array2 = numpy.roll(array, -1)
array3 = numpy.roll(array, -2)
sums = array[:-2] + array2[:-2] + array3[:-2]
increases = sums[1:] > sums[:-1]
print(sum(increases))
