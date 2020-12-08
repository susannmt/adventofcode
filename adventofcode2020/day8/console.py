instructions = [line.split() for line in open("input.txt").readlines()]


# part 1
acc = 0
idx = 0
visited = [idx]

while len(set(visited)) == len(visited):
    op, arg = instructions[idx]
    if op == "nop":
        idx += 1
    elif op == "acc":
        acc += int(arg)
        idx += 1
    elif op == "jmp":
        idx += (int(arg))
    visited.append(idx)

print(acc)

# part 2
for i in range(len(instructions)):
    if instructions[i][0] == "acc":
        continue

    acc = 0
    idx = 0
    visited = [idx]

    while len(set(visited)) == len(visited):
        op, arg = instructions[idx]

        if idx == i:
            op = "nop" if op == "jmp" else "jmp"

        if op == "nop":
            idx += 1
        elif op == "acc":
            acc += int(arg)
            idx += 1
        elif op == "jmp":
            idx += (int(arg))
        visited.append(idx)

        if idx == len(instructions):
            print(acc)
            break
