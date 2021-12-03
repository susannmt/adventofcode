import numpy
from scipy.stats import mode

report = []
for line in open("input.txt"):
    report.append(list(line.strip()))

report = numpy.array(report)


# part 1
frequent = mode(report, axis=0)[0][0]

gamma = int("".join([b for b in frequent]),2)
epsilon = int("".join([str(int(b=='0')) for b in frequent]),2)

print(gamma, epsilon, gamma*epsilon)


# part 2
oxygen = 0
co2 = 0

oxygen_candidates = report.copy()
for i in range(len(report[0])):
    if len(oxygen_candidates) <= 1:
        break

    nums, counts = mode(oxygen_candidates, axis=0)
    if counts[0][i] == len(oxygen_candidates)/2:
        freqs = '1'
    else:
        freqs = nums[0][i]

    oxygen_candidates = oxygen_candidates[numpy.where(oxygen_candidates[:, i] == freqs)]

oxygen = int("".join(oxygen_candidates[0]), 2)


co2_candidates = report.copy()
for i in range(len(report[0])):
    if len(co2_candidates) <= 1:
        break

    nums, counts = mode(co2_candidates, axis=0)
    if counts[0][i] == len(co2_candidates)/2:
        freqs = '0'
    else:
        freqs = str(int(nums[0][i] == '0'))

    co2_candidates = co2_candidates[numpy.where(co2_candidates[:, i] == freqs)]

co2 = int("".join(co2_candidates[0]), 2)

