import copy
banks = [int(block) for block in open("input.txt", "r").read().split()]
size = len(banks)


M = 0
states = []

while banks not in states:
    states.append(copy.deepcopy(banks))
    redistribute = max(banks)
    bank = banks.index(redistribute)
    banks[bank] = 0
    for i in range(bank+1, bank+1+redistribute):
        if i >= size:
            i -= size
        banks[i] += 1
    M += 1

print M

a = states.index(banks)
b = len(states)
print b-a

