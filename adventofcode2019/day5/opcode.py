
for noun in range(100):
    for verb in range(100):
        intcode = [int(num) for num in open("input.txt").read().split(",")]

        i = 0

        integer_input = 1
        while True:
            code = f"{intcode[i]:05}"
            opcode = int(code[-2:])
            m1, m2, m3 = [int(mode) for mode in code[2::-1]]

            if opcode == 99:
                break
            elif opcode == 1:
                param1 = i+1 if m1 else intcode[i+1]
                param2 = i+2 if m2 else intcode[i+2]
                param3 = i+3 if m3 else intcode[i+3]
                intcode[param3] = intcode[param1] + intcode[param2]
                i += 4
            elif opcode == 2:
                param1 = i+1 if m1 else intcode[i+1]
                param2 = i+2 if m2 else intcode[i+2]
                param3 = i+3 if m3 else intcode[i+3]
                intcode[param3] = intcode[param1] * intcode[param2]
                i += 4
            elif opcode == 3:
                param1 = i+1 if m1 else intcode[i+1]
                intcode[param1] = integer_input
                i += 2
            elif opcode == 4:
                param1 = i+1 if m1 else intcode[i+1]
                print(intcode[param1])
                i += 2
            else:
                print("unknown upcode")
                break

