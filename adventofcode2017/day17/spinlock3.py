import numpy as np

step = 335
#step = 3

circuit = [0]
current_position = 0

for i in range(1, 2018):

    move = (current_position + step) % len(circuit) + 1

    if move > len(circuit):
        move -= len(circuit)

    circuit[move:move] = [i]
    current_position = move


index = circuit.index(2017)
print circuit[index-2:index+3]

# zero always first, since we always extend
# after zero, those that have a current + step == length
# current pos == current length (add 1 when length is 1, 2 when lenght is 2 etc

current_position = 0
placed_after_zero = []
for i in range(1, 50000001):
    mv = (current_position + step) % (i)
    if mv == 0:
        placed_after_zero.append(i)

    current_position == mv

    if i % 10000 == 0:
        print i

print
print placed_after_zero
print placed_after_zero[-1]
