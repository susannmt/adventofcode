import copy

communicate = open("input.txt", 'r').readlines()
programs = {}

for i in range(len(communicate)):
    programs[i] = [int(w.strip(',')) for w in communicate[i].split()[2:]]


def get_group(ID):
    group = []
    stack = [ID]

    while stack:
        program = stack.pop()

        if program in group:
            continue

        stack += programs[program]
        group.append(program)

    return group


print len(get_group(0))

def get_all_groups():
    groups = []
    stack = range(len(communicate))

    while stack:
        program = stack.pop()
        group = get_group(program)

        for prog in group:
            if prog in stack:
                stack.remove(prog)

        groups.append(group)

    return groups

print len(get_all_groups())
