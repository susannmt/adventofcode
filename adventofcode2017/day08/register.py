from collections import defaultdict

instructions = open("input.txt", "r").readlines()
jump = {'inc': '+=', 'dec': '-='}
register = defaultdict(lambda:0)

largest = 0

for instruction in instructions:
    line = instruction.split()
    command = "register['%s'] %s %s if register['%s'] %s %s else 0" \
                %(line[0], jump[line[1]], line[2], line[4], line[5], line[6])
    exec(command)

    if max(register.values()) > largest:
        largest = max(register.values())

print max(register.values())
print largest
