horizontal = 0
depth = 0

# part 1
for line in open("input.txt").readlines():
    command, effect = line.split()
    if command == "forward":
        horizontal += int(effect)
    elif command == "down":
        depth += int(effect)
    elif command == "up":
        depth -= int(effect)

print(horizontal*depth)


# part 2
horizontal = 0
depth = 0
aim = 0

for line in open("input.txt").readlines():
    command, effect = line.split()
    if command == "forward":
        horizontal += int(effect)
        depth += int(effect)*aim
    elif command == "down":
        aim += int(effect)
    elif command == "up":
        aim -= int(effect)

print(horizontal*depth)
