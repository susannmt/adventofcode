from collections import deque
import numpy

with open("input.txt", "r") as input_file:
    tracks = [list(line.strip("\n")) for line in input_file.readlines()]


cart_syms = {">": "-", "v": "|", "<": "-", "^": "|"}
symbols = [">", "v", "<", "^"]
directions = {">": (0, 1), "v": (1, 0), "<": (0, -1), "^": (-1, 0)}


def turn(symbol, direction):
    if direction == "straight":
        return symbol

    index = symbols.index(symbol)
    if direction == "left":
        new = symbols[index-1]
    elif direction == "right":
        if index == 3:
            new = symbols[0]
        else:
            new = symbols[index+1]
    return new



class Cart():

    def __init__(self, i, j, symbol):
        self.position = (i, j)
        self.symbol = symbol
        self.direction = directions[symbol]
        self.turns = deque(["left", "straight", "right"])
        self.removed = False

    def move(self):
        x = self.position[0] + self.direction[0]
        y = self.position[1] + self.direction[1]

        if tracks[x][y] in ["|", "-"]:
            self.symbol = turn(self.symbol, "straight")

        elif tracks[x][y] == "/":

            if self.symbol in ["^", "v"]:
                self.symbol = turn(self.symbol, "right")

            else:
                self.symbol = turn(self.symbol, "left")

        elif tracks[x][y] == "+":
            self.symbol = turn(self.symbol, self.turns[0])
            self.turns.rotate(-1)

        else:
            if self.symbol in ["^", "v"]:
                self.symbol = turn(self.symbol, "left")
            else:
                self.symbol = turn(self.symbol, "right")

        self.position = x, y
        self.direction = directions[self.symbol]

    def remove(self):
        self.removed = True


carts = []
cart_map = numpy.empty((len(tracks), len(tracks[0])), dtype=Cart)
for i in range(len(tracks)):
    for j in range(len(tracks[0])):
        if tracks[i][j] in cart_syms:
            cart = tracks[i][j]
            tracks[i][j] = cart_syms[cart]
            cart_object = Cart(i, j, cart)
            carts.append(cart_object)
            cart_map[i, j] = cart_object

def extract_order(cart_map):
    order = []
    for i in range(cart_map.shape[0]):
        for j in range(cart_map.shape[1]):
            if cart_map[i,j] is not None:
                if cart_map[i,j].removed:
                    cart_map[i,j] = None
                else:
                    order.append(cart_map[i,j])
    return order


print(len(carts))
while len(carts) > 1:
    positions = numpy.zeros((len(tracks), len(tracks[0])))
    carts_in_order = extract_order(cart_map)
    for cart in carts_in_order:
        if cart.removed:
            continue

        prev_pos = cart.position
        cart_map[prev_pos] = None
        cart.move()
        new_pos = cart.position
        positions[new_pos] += 1

        if cart_map[new_pos] is not None:
            print("crash", new_pos[1], new_pos[0])
            cart_map[new_pos].remove()
            cart.remove()
        else:
            cart_map[new_pos] = cart

    carts = [c for c in carts_in_order if not c.removed]

print("final", carts[0].position[1], carts[0].position[0])
