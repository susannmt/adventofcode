import numpy

def run_intcode(integer_input: int, play_for_free: bool = False):
    intcode_input = [int(num) for num in open("input.txt").read().split(",")]
    intcode = numpy.zeros(10000000, dtype=int)
    intcode[:len(intcode_input)] = intcode_input

    if play_for_free:
        intcode[0] = 2

    i = 0
    relative_base = 0
    output = []
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
            i += 2

        elif opcode == 4:
            param1 = i+1 if m1 == 1 else intcode[i+1]
            if m1 == 2:
                param1 += relative_base
            output.append(intcode[param1])
            if len(output) > 2 and len(output)//2 == 0 :
                if output[-3] == -1 and output[-2] == 0:
                    print(f"score {output[-1]}")
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
    outseq = run_intcode(0)
    tiles = {}
    for i in range(0, len(outseq), 3):
        position = (outseq[i], outseq[i+1])
        tiles[position] = outseq[i+2]

    print(list(tiles.values()).count(2))


