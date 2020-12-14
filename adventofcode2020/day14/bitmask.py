from collections import defaultdict
from itertools import product

with open("input.txt") as handle:
    instructions = handle.readlines()

# part 1
memory = defaultdict(int)
mask = "X"*36
for instruction in instructions:
    if instruction.startswith("mask"):
        mask = instruction.split()[-1]
        continue

    pos, _, val = instruction.split()
    pos = int(pos[4:-1])
    val = f"{int(val):036b}"
    val = "".join([val[i] if mask[i] == "X" else mask[i] for i in range(36)])
    memory[pos] = int(val, 2)

print(sum(memory.values()))

# part 2
memory = defaultdict(int)
mask = "0"*36
floats = 0

for instruction in instructions:
    if instruction.startswith("mask"):
        mask = instruction.split()[-1]
        floats = [i for i in range(36) if mask[i] == "X"]
        continue

    pos, _, val = instruction.split()
    val = int(val)
    pos = f"{int(pos[4:-1]):036b}"
    pos = [mask[i] if mask[i] == "X" else str(int(pos[i])|int(mask[i])) for i in range(36)]

    for bits in product([0,1], repeat=len(floats)):
        pos_ = pos.copy()
        for i, bit in zip(floats, bits):
            pos_[i] = str(bit)
        pos_ = "".join(pos_)
        memory[int(pos_, 2)] = val

print(sum(memory.values()))
