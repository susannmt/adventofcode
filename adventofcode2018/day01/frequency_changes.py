with open("input.txt", "r") as input_file:
    changes = [int(line) for line in input_file.readlines()]
print(sum(changes))

frequency = 0
results = [0]
for change in changes*500:
    frequency += change
    results.append(frequency)
    if len(set(results)) != len(results):
        print(frequency)
        break
