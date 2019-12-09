import numpy

def run_boost(integer_input: int):
    intcode_input = [int(num) for num in open("input.txt").read().split(",")]
    intcode = numpy.zeros(10000000, dtype=int)
    intcode[:len(intcode_input)] = intcode_input

    i = 0
    relative_base = 0
    output = None
    while True:
        code = f"{intcode[i]:05}"
        opcode = int(code[-2:])
        m1, m2, m3 = [int(mode) for mode in code[2::-1]]

        if opcode == 99:
            return output

        elif opcode == 1:
            param1 = i+1 if m1 == 1 else intcode[i+1]
            param2 = i+2 if m2 == 1 else intcode[i+2]
            param3 = i+3 if m3 == 1 else intcode[i+3]
            if m1 == 2:
                param1 += relative_base
            if m2 == 2:
                param2 += relative_base
            if m3 == 2:
                param3 += relative_base
            intcode[param3] = intcode[param1] + intcode[param2]
            i += 4

        elif opcode == 2:

            param1 = i+1 if m1 == 1 else intcode[i+1]
            param2 = i+2 if m2 == 1 else intcode[i+2]
            param3 = i+3 if m3 == 1 else intcode[i+3]
            if m1 == 2:
                param1 += relative_base
            if m2 == 2:
                param2 += relative_base
            if m3 == 2:
                param3 += relative_base
            intcode[param3] = intcode[param1] * intcode[param2]
            i += 4

        elif opcode == 3:
            param1 = i+1 if m1 == 1 else intcode[i+1]
            if m1 == 2:
                param1 += relative_base
            intcode[param1] = integer_input
            has_started = True
            i += 2

        elif opcode == 4:
            param1 = i+1 if m1 == 1 else intcode[i+1]
            if m1 == 2:
                param1 += relative_base
            output = intcode[param1]
            print(output)
            i += 2

        elif opcode == 5:
            param1 = i+1 if m1 == 1 else intcode[i+1]
            if m1 == 2:
                param1 += relative_base
            if intcode[param1]:
                param2 = i+2 if m2 == 1 else intcode[i+2]
                if m2 == 2:
                    param2 += relative_base
                i = intcode[param2]
            else:
                i += 3

        elif opcode == 6:
            param1 = i+1 if m1 == 1 else intcode[i+1]
            if m1 == 2:
                param1 += relative_base
            if not intcode[param1]:
                param2 = i+2 if m2 == 1 else intcode[i+2]
                if m2 == 2:
                    param2 += relative_base
                i = intcode[param2]
            else:
                i += 3

        elif opcode == 7:
            param1 = i+1 if m1 == 1 else intcode[i+1]
            param2 = i+2 if m2 == 1 else intcode[i+2]
            param3 = i+3 if m3 == 1 else intcode[i+3]
            if m1 == 2:
                param1 += relative_base
            if m2 == 2:
                param2 += relative_base
            if m3 == 2:
                param3 += relative_base
            intcode[param3] = int(intcode[param1] < intcode[param2])
            i += 4

        elif opcode == 8:
            param1 = i+1 if m1 == 1 else intcode[i+1]
            param2 = i+2 if m2 == 1 else intcode[i+2]
            param3 = i+3 if m3 == 1 else intcode[i+3]
            if m1 == 2:
                param1 += relative_base
            if m2 == 2:
                param2 += relative_base
            if m3 == 2:
                param3 += relative_base
            intcode[param3] = int(intcode[param1] == intcode[param2])
            i += 4

        elif opcode == 9:
            param1 = i+1 if m1 == 1 else intcode[i+1]
            if m1 == 2:
                param1 += relative_base
            relative_base += intcode[param1]
            i += 2

        else:
            print("unknown opcode")
            return


if __name__ == '__main__':
    run_boost(1)
    run_boost(2)
