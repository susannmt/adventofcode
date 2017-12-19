from collections import defaultdict

commands = open("input.txt", "r").readlines()

def part1():
    register = defaultdict(int)
    freq = None

    i = 0
    while 0 <= i < len(commands):
        command = commands[i].split()

        # get values
        if len(command) == 3:
            if command[2].isalpha():
                command[2] = register[command[2]]
            else:
                command[2] = int(command[2])

        if command[0] == 'snd':
            freq = register[command[1]]

        elif command[0] == 'set':
            register[command[1]] = int(command[2])

        elif command[0] == 'add':
            register[command[1]] += command[2]

        elif command[0] == 'mul':
            register[command[1]] *= command[2]

        elif command[0] == 'mod':
            register[command[1]] = register[command[1]] % command[2]

        elif command[0] == 'rcv':
            if register[command[1]] != 0:
                return freq

        elif command[0] == 'jgz':
            if register[command[1]] > 0:
                i += command[2]
                continue

        i += 1

print part1()


def part2():

    def getval(c, reg):
        if c.isalpha():
            return reg[c]
        else:
            return int(c)

    registers = [defaultdict(int), defaultdict(int)]
    registers[0]['p'] = 0
    registers[1]['p'] = 1

    queue = [[],[]]

    k = 0
    j = 0

    reg1wait = False
    reg2wait = False

    def preform(nr, i, res):

        reg = registers[nr]

        if 0 <= i < len(commands):
            command = commands[i].split()

            if command[0] == 'snd':

                if nr == 0:
                    queue[1].append(getval(command[1], reg))
                    res += 1

                else:
                    queue[0].append(getval(command[1], reg))


            elif command[0] == 'set':
                reg[command[1]] = getval(command[2], reg)

            elif command[0] == 'add':
                reg[command[1]] += getval(command[2], reg)

            elif command[0] == 'mul':
                reg[command[1]] *= getval(command[2], reg)

            elif command[0] == 'mod':
                reg[command[1]] = reg[command[1]] \
                                            % getval(command[2], reg)

            elif command[0] == 'rcv':

                if queue[nr]:
                    reg[command[1]] = queue[nr].pop(0)

                else:
                    return i, True, res # wait

            elif command[0] == 'jgz':
                if reg[command[1]] > 0:
                    i += getval(command[2], reg)
                    return i, False, res

            else:
                print "out of bounds"
                return i, True, res # out of bounds

            return i + 1, False, res

    res = 0
    while not (reg1wait and reg2wait):
        k, reg1wait, res = preform(0, k, res)
        j, reg2wait, _   = preform(1, j, res)

    return res

print part2()


