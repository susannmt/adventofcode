import numpy

with open("input.txt", "r") as input_file:
    ids = input_file.readlines()

count2 = 0
count3 = 0
for box_id in ids:
    counts = [box_id.count(char) for char in set(list(box_id))]
    count2 += 2 in counts
    count3 += 3 in counts

print(count2*count3)

for i in range(len(ids)):
    for j in range(i+1, len(ids)):
        box1 = numpy.array(list(ids[i]))
        box2 = numpy.array(list(ids[j]))

        diff = sum(box1 != box2)
        if diff == 1:
            print(box1[box1==box2])


