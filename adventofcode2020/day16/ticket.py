import numpy
with open("input.txt") as handle:
    sections = handle.read().split("\n\n")
    rules = {}
    for line in sections[0].split("\n"):
        field, values = line.split(":")
        values = values.split(" or ")
        ranges = [values[0].split("-"), values[1].split("-")]
        ranges = [list(range(int(l[0]), int(l[1])+1)) for l in ranges]
        rules[field] = ranges[0] + ranges[1]

    your_ticket = [int(num) for num in sections[1].split("\n")[1].split(",")]

    nearby_tickets = []
    for line in sections[2].strip().split("\n"):
        if line.startswith("nearby"):
            continue
        nearby_tickets.append([int(num) for num in line.split(",")])

not_valid = []
valid_tickets = []
for ticket in nearby_tickets:
    for value in ticket:
        for valid in rules.values():
            if value in valid:
                break
        else:
            not_valid.append(value)
            break
    else:
        valid_tickets.append(ticket)

print(sum(not_valid))

valid_tickets = numpy.array(valid_tickets)
possible_meanings = {}
for key, valid in rules.items():
    possible_meanings[key] = []
    for i in range(len(rules)):
        if numpy.isin(valid_tickets[:,i], valid).all():
            possible_meanings[key].append(i)

result = {}
while len(result) < len(rules):
    for key, options in possible_meanings.items():
        if len(options) == 1:
            result[key] = options[0]
            for k, o in possible_meanings.items():
                possible_meanings[k] = [num for num in o if num != options[0]]
            possible_meanings.pop(key)
            break
print(numpy.prod([your_ticket[v] for k,v in result.items() if k.startswith("departure")]))
