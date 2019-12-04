import numpy

passwords1 = set()
passwords2 = set()
for number in range(100000, 1000000):
    number = ''.join(sorted(str(number)))

    if int(number) in range(178416, 676469):
        if len(set(number)) < 6:
            passwords1.add(number)
        value, count = numpy.unique(list(number), return_counts=True)
        if 2 in count:
            passwords2.add(number)

print(len(passwords1))
print(len(passwords2))

