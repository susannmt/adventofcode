
valid = 0
valid2 = 0
with open("input.txt", "r") as handle:
    for line in handle.readlines():
        policy, letter, password = line.split()
        lower, upper = policy.split("-")
        letter = letter.strip(":")
        count = password.count(letter)

        if count <= int(upper) and count >= int(lower):
            valid += 1

        first = int(password[int(lower)-1] == letter)
        second = int(password[int(upper)-1] == letter)

        if first+second == 1:
            valid2 += 1


print(valid)
print(valid2)
