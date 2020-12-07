rules = {}

with open("input.txt") as handle:
    for rule in handle.readlines():
        rule = rule.split()
        main_bag = "_".join(rule[0:2])
        content = {}
        i = 2
        while i < len(rule)-2:
            if rule[i].isnumeric():
                content["_".join(rule[i+1:i+3])] = int(rule[i])
                i += 3
            else:
                i += 1
        rules[main_bag] = content

# part 1
my_bag = "shiny_gold"
parent_bag_list = set()
parent_bag_list2 = set()

for bag in rules:
    if my_bag in rules[bag]:
        parent_bag_list2.add(bag)

while len(parent_bag_list) != len(parent_bag_list2):
    parent_bag_list = parent_bag_list2.copy()

    for bag in rules:
        if parent_bag_list.intersection(rules[bag].keys()):
            parent_bag_list2.add(bag)

print(len(parent_bag_list))

def count_children(bag, nr_of_that_bag):
    if not rules[bag]:
        return nr_of_that_bag

    content = 0
    for child_bag, nr_of_child_bag in rules[bag].items():
        content += count_children(child_bag, nr_of_child_bag)

    return content*nr_of_that_bag + nr_of_that_bag


print(count_children(my_bag, 1) - 1)
