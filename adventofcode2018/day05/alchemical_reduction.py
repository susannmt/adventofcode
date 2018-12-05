with open("input.txt", "r") as input_file:
    polymers = input_file.read().strip()

def reacting(polymer):
    while True:
        i = 0
        remove_indices = []
        while i < len(polymer) - 1:
            if polymer[i+1] == polymer[i].swapcase():
                remove_indices += [i, i+1]
                i += 2
            else:
                i += 1

        if not remove_indices:
            return polymer, len(polymer)

        polymer = ''.join([polymer[i] for i in range(len(polymer))
                            if i not in remove_indices])

# part 1
units, length = reacting(polymers)
print(length)

# part 2
for char in set(list(units.lower())):
    polymer = units.replace(char, '').replace(char.upper(), '')
    print(char, reacting(polymer)[1])

