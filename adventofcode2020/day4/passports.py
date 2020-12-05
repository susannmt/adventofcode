import re

# read data
passports = []
with open("input.txt", "r") as handle:
    passport = {}
    for line in handle.readlines():
        if line == "\n":
            passports.append(passport)
            passport = {}
        else:
            for item in line.strip().split():
                key, val = item.split(":")
                passport[key] = val
    passports.append(passport)

# check validity part 1
required = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
valid = 0
for passport in passports:
    if required.issubset(passport.keys()):
        valid += 1

print(valid)

# part 2
valid = 0
for passport in passports:
    if not required.issubset(passport.keys()):
        continue
    if not 1920 <= int(passport["byr"]) <= 2002:
        continue
    if not 2010 <= int(passport["iyr"]) <= 2020:
        continue
    if not 2020 <= int(passport["eyr"]) <= 2030:
        continue
    if "in" in passport["hgt"]:
        if not 59 <= int(passport["hgt"][:-2]) <= 76:
            continue
    elif "cm" in passport["hgt"]:
        if not 150 <= int(passport["hgt"][:-2]) <= 193:
            continue
    else:
        continue
    if re.match("#[0-9a-f]{6}", passport["hcl"]) is None:
        continue
    if passport["ecl"] not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
        continue
    if len(passport["pid"]) != 9 or re.match("\d{9}", passport["pid"]) is None:
        continue
    valid += 1

print(valid)
