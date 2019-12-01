modules = open("input.txt").readlines()

fuel_requirements1 = 0
fuel_requirements2 = 0

for module in modules:
    module = int(module)
    fuel_amount =  int(int(module) / 3) - 2
    fuel_requirements1 += fuel_amount
    while fuel_amount > 0:
        fuel_requirements2 += fuel_amount
        fuel_amount = int(fuel_amount / 3) - 2

print(fuel_requirements1)
print(fuel_requirements2)
