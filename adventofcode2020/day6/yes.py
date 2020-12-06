with open("input.txt") as handle:
    groups = handle.read().split("\n\n")

count1 = 0
count2 = 0
for group in groups:
    yeses = [list(questions) for questions in group.split("\n")]
    yeses = list(filter(None, yeses))

    # part 1 - how many anyone answered
    unique = set(sum(yeses, []))
    count1 += len(unique)

    # part 2 - how many everyone answered
    shared = set(yeses[0]).intersection(*yeses[1:])
    count2 += len(shared)

print(count1)
print(count2)
