from datetime import datetime
import numpy

with open("input.txt", "r") as input_file:
    stamps = [(datetime.strptime(l[:18], "[%Y-%m-%d %H:%M]"), l[19:]) for l in
                input_file.readlines()]

sorted_stamps = sorted(stamps, key=lambda tup: tup[0])

sleeping = {}
current_id = None
current_slice_start = None
for timestamp in sorted_stamps:
    if timestamp[1].startswith("Guard"):
        current_id = int(timestamp[1].split()[1][1:])
        if current_id not in sleeping:
            sleeping[current_id] = numpy.zeros(60)
    elif timestamp[1].startswith("falls"):
        current_slice_start = int(timestamp[0].minute)
    elif timestamp[1].startswith("wakes"):
        sleeping[current_id][current_slice_start:int(timestamp[0].minute)] += 1
        current_slice_start = None

for guard_id, sleep in sleeping.items():
    print(guard_id, sum(sleep), max(sleep), guard_id*numpy.argmax(sleep))

