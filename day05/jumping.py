import copy

offsets = [int(jump) for jump in open("input.txt", "r").readlines()]
L = len(offsets)


off1 = copy.deepcopy(offsets)
M = 0
i = 0
while 0 <= i < L:
    jump = off1[i]
    off1[i] += 1
    i += jump
    M += 1

print M



off2 = copy.deepcopy(offsets)
M = 0
i = 0
while 0 <= i < L:
    jump = off2[i]
    if off2[i] >= 3:
        off2[i] -= 1
    else:
        off2[i] += 1
    i += jump
    M += 1

print M
