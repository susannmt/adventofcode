puzzle_input = 236021
#puzzle_input = 2018
scores = [3, 7, 1, 0, 1, 0, 1, 2]
n = len(scores)
elf0 = 0
elf1 = 6

while n < 100000000:
    combined = str(scores[elf0] + scores[elf1])
    scores.append(int(combined[0]))
    n += 1
    if len(combined) == 2:
        scores.append(int(combined[1]))
        n += 1

    elf0 += scores[elf0] + 1
    elf1 += scores[elf1] + 1

    elf0 = elf0 % n
    elf1 = elf1 % n


#print("".join([str(s) for s in scores[-10:]]))

score_string = "".join([str(s) for s in scores])
print(score_string[puzzle_input:puzzle_input+10])
print(score_string.find(str(puzzle_input)))

