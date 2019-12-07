from itertools import permutations

def run_amplifier(integer_input: int, phase_setting: int):
    intcode = [int(num) for num in open("input.txt").read().split(",")]

    i = 0
    output = None
    has_started = False
    while True:
        code = f"{intcode[i]:05}"
        opcode = int(code[-2:])
        m1, m2, m3 = [int(mode) for mode in code[2::-1]]

        if opcode == 99:
            return output
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
            intcode[param1] = integer_input if has_started else phase_setting
            has_started = True
            i += 2
        elif opcode == 4:
            param1 = i+1 if m1 else intcode[i+1]
            output = intcode[param1]
            i += 2
        elif opcode == 5:
            param1 = i+1 if m1 else intcode[i+1]
            if intcode[param1]:
                param2 = i+2 if m2 else intcode[i+2]
                i = intcode[param2]
            else:
                i += 3
        elif opcode == 6:
            param1 = i+1 if m1 else intcode[i+1]
            if not intcode[param1]:
                param2 = i+2 if m2 else intcode[i+2]
                i = intcode[param2]
            else:
                i += 3
        elif opcode == 7:
            param1 = i+1 if m1 else intcode[i+1]
            param2 = i+2 if m2 else intcode[i+2]
            param3 = i+3 if m3 else intcode[i+3]
            intcode[param3] = int(intcode[param1] < intcode[param2])
            i += 4
        elif opcode == 8:
            param1 = i+1 if m1 else intcode[i+1]
            param2 = i+2 if m2 else intcode[i+2]
            param3 = i+3 if m3 else intcode[i+3]
            intcode[param3] = int(intcode[param1] == intcode[param2])
            i += 4
        else:
            print("unknown opcode")
            return


if __name__ == '__main__':
    thruster_signals = []
    for phase_settings in permutations([0,1,2,3,4]):
        ampA = run_amplifier(0, phase_settings[0])
        ampB = run_amplifier(ampA, phase_settings[1])
        ampC = run_amplifier(ampB, phase_settings[2])
        ampD = run_amplifier(ampC, phase_settings[3])
        ampE = run_amplifier(ampD, phase_settings[4])
        thruster_signals.append(ampE)
    print(thruster_signals)
    print(max(thruster_signals))

