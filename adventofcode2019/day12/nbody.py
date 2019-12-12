from itertools import combinations

moons = []
velocities = []
for line in open("input.txt").readlines():
    positions = line.strip()[1:-1].split(",")
    x, y, z = [int(pos.split("=")[-1]) for pos in positions]
    moons.append([x,y,z])
    velocities.append([0,0,0])

pairs = list(combinations(range(4), 2))
for t in range(1000):

    for m1, m2 in pairs:
        for i in range(3):
            if moons[m1][i] > moons[m2][i]:
                velocities[m1][i] -= 1
                velocities[m2][i] += 1
            elif moons[m1][i] < moons[m2][i]:
                velocities[m2][i] -= 1
                velocities[m1][i] += 1

    for m in range(4):
        moons[m][0] += velocities[m][0]
        moons[m][1] += velocities[m][1]
        moons[m][2] += velocities[m][2]

energy = 0
for m in range(4):
    pot = sum(map(abs, moons[m]))
    kin = sum(map(abs, velocities[m]))
    energy += pot*kin
print(energy)



