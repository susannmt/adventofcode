import numpy

geology = []
with open("input.txt", "r") as handle:
    for line in handle.readlines():
        geology.append(list(line.strip()))
geology = numpy.array(geology)

x = len(geology)
y = len(geology[0])

# part 1
i = 0
j = 0

trees = 0
while i < x:
    if j >= y:
        j = j - y
    trees += geology[i][j] == "#"
    i += 1
    j += 3

print(trees)

# part 2
rules = (1,1), (1,3), (1,5), (1,7), (2,1)
results = []
for rule in rules:
    i = 0
    j = 0

    trees = 0
    while i < x:
        if j >= y:
            j = j - y
        trees += geology[i][j] == "#"
        i += rule[0]
        j += rule[1]

    results.append(trees)

print(numpy.prod(results))
