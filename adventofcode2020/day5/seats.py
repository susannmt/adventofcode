#boarding_passes = ["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
with open("input.txt") as handle:
    boarding_passes = handle.readlines()

seat_IDs = []
for boarding_pass in boarding_passes:
    rows = range(0, 128)
    for i in range(7):
        half = round(len(rows) / 2)
        rows = rows[:half] if boarding_pass[i] == "F" else rows[half:]

    columns = range(0,8)
    for i in range(7,10):
        half = round(len(columns) / 2)
        columns = columns[:half] if boarding_pass[i] == "L" else columns[half:]

    seat_ID = rows[0]*8+columns[0]
    seat_IDs.append(seat_ID)

print(max(seat_IDs))
seat_IDs = set(seat_IDs)
all_IDs = set(range(min(seat_IDs), max(seat_IDs)+1))
print(all_IDs.difference(seat_IDs))
