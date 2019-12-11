import numpy

class Robot:
    def __init__(self):
        intcode_input = [int(num) for num in open("input.txt").read().split(",")]
        self.intcode = numpy.zeros(10000000, dtype=int)
        self.intcode[:len(intcode_input)] = intcode_input
        self.i = 0
        self.relative_base = 0
        self.direction_map = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0,-1)}
        self.panels = numpy.zeros((200, 200))
        self.x = 100
        self.y = 100
        self.directions = numpy.array(["^", ">", "v", "<"])
        self.painted = set()

        finished = 0
        while not finished:
            finished = self.move()

        for i in range(200):
            sign = []
            for j in range(200):
                panel = "#" if self.panels[i][j] else " "
                sign.append(panel)
            print("".join(sign))

        print(len(self.painted))

    def move(self):
        current_panel = self.panels[self.x, self.y]
        result = self.run_intcode(current_panel)

        if not len(result) == 2:
            return 1

        paint_color, turn = result
        self.panels[self.x, self.y] = paint_color
        self.painted.add((self.x, self.y))

        movement = self.direction_map[self.directions[0]]
        self.x = self.x + movement[0]
        self.y = self.y + movement[1]
        if turn:
            self.directions = numpy.roll(self.directions, -1)
        else:
            self.directions = numpy.roll(self.directions, 1)

        return 0




    def run_intcode(self, integer_input: int):

        intcode = self.intcode
        i = self.i
        relative_base = self.relative_base

        output = []
        while True:
            if len(output) == 2:
                break

            code = f"{intcode[i]:05}"
            opcode = int(code[-2:])
            m1, m2, m3 = [int(mode) for mode in code[2::-1]]

            if opcode == 99:
                break

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
                break

        self.i = i
        self.intcode = intcode
        self.relative_base = relative_base

        return output

if __name__ == '__main__':
    Robot()
