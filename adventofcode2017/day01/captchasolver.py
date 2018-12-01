# Find the sum of all digits that match the next digit in the list.

captcha = open("input.txt", "r").read().strip()
sol = 0

# loop thorugh
for i in range(len(captcha)-1):
    if captcha[i] == captcha[i+1]:
        sol += int(captcha[i])

# circularity
if captcha[-1] == captcha[0]:
    sol += int(captcha[-1])

print sol
