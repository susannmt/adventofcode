from collections import Counter

path = open("input.txt", "r").read().strip().split(',')

# --- PART 1 ---

occ1 = Counter(path)

def distance(occ):

    for one, two in [('s', 'n'), ('sw', 'ne'), ('se', 'nw')]:
        larger = one if occ[one] > occ[two] else two
        smallr = two if occ[one] > occ[two] else one
        occ[larger] = occ[larger]-occ[smallr]
        occ[smallr] = 0

    dirs = []
    for direction, steps in occ.iteritems():
        if steps != 0:
            dirs.append(direction)

    triplets = ('nw', 'n', 'ne'), ('n', 'ne', 'se'), ('ne', 'se', 's'), \
               ('se', 's', 'sw'), ('s', 'sw', 'nw'), ('sw', 'nw', 'n')

    for trip in triplets:
        if trip[0] in dirs and trip[1] in dirs and trip[2] in dirs:
            break

    while occ[trip[0]] > 0 and occ[trip[-1]] > 0:
        occ[trip[0]] -= 1
        occ[trip[-1]] -= 1
        occ[trip[1]] += 1

    return sum(occ.values())

print distance(occ1)

# --- PART 2 ---
furthest = 0
for n in range(1, len(path)):
    occ2 = Counter(path[:n])
    dist = distance(occ2)
    if dist > furthest:
        furthest = dist

print furthest


