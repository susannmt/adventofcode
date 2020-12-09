import itertools
nums = [int(nr) for nr in open("input.txt").readlines()]

l = 25

invalid = None
for i in range(l,len(nums)):
    target = nums[i]
    preamble = nums[i-l:i]
    for numbers in itertools.combinations(preamble, 2):
        if sum(numbers) == target:
            break
    else:
        invalid = target

print(invalid)


for start, stop in itertools.combinations(range(len(nums)+1), 2):
    if sum(nums[start:stop]) == invalid:
        print(sum([min(nums[start:stop]), max(nums[start:stop])]))
        break
