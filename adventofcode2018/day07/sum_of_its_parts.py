from collections import defaultdict

instructions = defaultdict(list)
instructions2 = defaultdict(list)

with open("input.txt", "r") as input_file:
    for line in input_file.readlines():
        requirement, instruction = line.split()[1], line.split()[7]
        instructions[instruction].append(requirement)
        instructions2[instruction].append(requirement)
        if requirement not in instructions:
            instructions[requirement] = []
            instructions2[requirement] = []

steps = []
while len(instructions.keys()) > 0:
    for instruction in sorted(instructions.keys()):
        if len(instructions[instruction]) == 0:
            steps.append(instruction)
            instructions.pop(instruction)
            for other_instruction in instructions.keys():
                if instruction in instructions[other_instruction]:
                    idx = instructions[other_instruction].index(instruction)
                    instructions[other_instruction].pop(idx)
            break

print("".join(steps))

instructions = instructions2
time = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
seconds = -1
pending = {}

while len(instructions.keys()) > 0:

    seconds += 1

    for instruction in list(pending.keys()):
        pending[instruction] -= 1
        if pending[instruction] == 0:
            pending.pop(instruction)
            instructions.pop(instruction)
            for other_instruction in instructions.keys():
                if instruction in instructions[other_instruction]:
                    idx = instructions[other_instruction].index(instruction)
                    instructions[other_instruction].pop(idx)

    if len(pending.keys()) >= 5:
        continue

    for instruction in sorted(instructions.keys()):
        if instruction in pending:
            continue

        if len(instructions[instruction]) == 0:
            pending[instruction] = 60 + time.index(instruction) + 1

            if len(pending.keys()) >= 5:
                break

print(seconds)
