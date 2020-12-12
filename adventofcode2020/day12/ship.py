import collections

instructions = [(instruction[0], int(instruction[1:])) for instruction in
        open("input.txt").readlines()]


# part 1
face = collections.deque(["E", "N", "W", "S"])
actions = {"N": (-1,0), "S": (1,0), "E": (0,1), "W": (0,-1)}
position = [0, 0]

for action, value in instructions:
    if action == "F":
        position[0] += actions[face[0]][0]*value
        position[1] += actions[face[0]][1]*value
    elif action == "L":
        face.rotate(-int(value / 90))
    elif action == "R":
        face.rotate(int((value / 90)))
    else:
        position[0] += actions[action][0]*value
        position[1] += actions[action][1]*value

print(abs(position[0])+abs(position[1]))

# part 2
position = [0,0]
waypoint = [-1,10]


for action, value in instructions:
    if action == "F":
        position[0] += waypoint[0]*value
        position[1] += waypoint[1]*value

    elif action == "L":
        way = waypoint
        if value == 90:
            way = [-waypoint[1], waypoint[0]]
        if value == 180:
            way = [-waypoint[0], -waypoint[1]]
        if value == 270:
            way = [waypoint[1], -waypoint[0]]
        waypoint = way

    elif action == "R":
        way = waypoint
        if value == 90:
            way = [waypoint[1], -waypoint[0]]
        if value == 180:
            way = [-waypoint[0], -waypoint[1]]
        if value == 270:
            way = [-waypoint[1], waypoint[0]]
        waypoint = way
    else:
        waypoint[0] += actions[action][0]*value
        waypoint[1] += actions[action][1]*value

print(abs(position[0])+abs(position[1]))
