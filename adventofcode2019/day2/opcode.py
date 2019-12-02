
for noun in range(100):
    for verb in range(100):
        intcode = [int(num) for num in open("input.txt").read().split(",")]

        intcode[1] = noun
        intcode[2] = verb
        i = 0

        while True:
            if intcode[i] == 99:
                break
            elif intcode[i] == 1:
                intcode[intcode[i+3]] = intcode[intcode[i+2]] + intcode[intcode[i+1]]
                i += 4
            elif intcode[i] == 2:
                intcode[intcode[i+3]] = intcode[intcode[i+2]] * intcode[intcode[i+1]]
                i += 4
            else:
                print("unknown upcode")
                break

        if noun == 12 and verb == 2:
            print(intcode[0])

        if intcode[0] == 19690720:
            print(100*noun+verb)

