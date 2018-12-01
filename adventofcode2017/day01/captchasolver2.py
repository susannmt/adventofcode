# Find the sum of all digits that match the digit halfway around the list.

captcha = open("input.txt", "r").read().strip()
end = len(captcha)
half = end/2

sol = 0

# loop thorugh
for i in range(len(captcha)):
    halfway = i + half
    if halfway >= end:
        halfway -= end

    if captcha[i] == captcha[halfway]:
        sol += int(captcha[i])

print sol
