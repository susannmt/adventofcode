import numpy
room = [list(row.strip()) for row in open("input.txt").readlines()]
room = numpy.array(room)
original_room = room.copy()
hight = len(room)
width = len(room[0])

# part 1
new_room = room.copy()
room_adjacency = numpy.zeros((hight, width)).tolist()

for y in range(hight):
    for x in range(width):
        seat = original_room[y,x]
        if seat == ".":
            room_adjacency[y][x] = []
            continue
        else:
            coords = [(y+j,x+i) for i in (-1, 0, 1) for j in (-1, 0, 1)]
            room_adjacency[y][x] = [coor for coor in coords if coor[0] in
                    range(hight) and coor[1] in range(width) and coor != (y,x)]


while True:
    new_room = room.copy()
    for y in range(hight):
        for x in range(width):
            seat = room[y,x]
            adjacent = [room[places] for places in room_adjacency[y][x]]
            if seat == "L" and "#" not in adjacent:
                new_room[y,x] = "#"

            if seat == "#" and adjacent.count("#") >= 4:
                new_room[y,x] = "L"

    if numpy.array_equal(new_room, room):
        break
    room = new_room.copy()

print(sum(sum(new_room == "#")))


# part 2
visible_seats = numpy.zeros((hight, width)).tolist()

for y in range(hight):
    for x in range(width):
        if original_room[y,x] == ".":
            visible_seats[y][x] = []
            continue
        else:
            visible = []
            directions = [(-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (1,1),(0,1),(-1,1)]
            for direction in directions:
                y_ = y + direction[0]
                x_ = x + direction[1]
                while y_ in range(hight) and x_ in range(width):
                    if original_room[y_, x_] != ".":
                        visible.append((y_, x_))
                        break
                    y_ += direction[0]
                    x_ += direction[1]
            visible_seats[y][x] = visible

room = original_room.copy()
while True:
    new_room = room.copy()
    for y in range(hight):
        for x in range(width):
            seat = room[y,x]
            visible = [room[places] for places in visible_seats[y][x]]
            if seat == "L" and "#" not in visible:
                new_room[y,x] = "#"

            if seat == "#" and visible.count("#") >= 5:
                new_room[y,x] = "L"

    if numpy.array_equal(new_room, room):
        break
    room = new_room.copy()

print(sum(sum(new_room == "#")))
