from collections import defaultdict, Counter

discs = open("input.txt", "r").readlines()
circus = defaultdict(list)
weight = defaultdict(int)
under = defaultdict(str)

for line in discs:
    l = line.split()
    weight[l[0]] = int(l[1][1:-1])

    if len(l) > 2:
        words = [w.strip(',') for w in l[3:]]
        circus[l[0]] = words
        for w in words:
            under[w] = l[0]


# --- PART 1 ---
curr = under['irrpz']
while curr != '':
    print curr
    curr = under[curr]

# --- PART 2 ---

root = 'mwzaxaj' # output from part 1... not prettiest handling


def get_balance(root):

    if circus[root] == []:
        return weight[root]


    return weight[root] + sum([get_balance(kid) for kid in circus[root]])


base = root
print base
while base != '':
    kids = circus[base]
    bal = [get_balance(b) for b in kids]
    print bal
    counter = Counter(bal)
    odd_index = bal.index(min(counter, key=counter.get))
    print odd_index
    base = kids[odd_index]
    print base



