
firewall = open("input.txt", "r").readlines()
layers = {}
for line in firewall:
    l = line.split()
    layers[int(l[0].strip(':'))] = int(l[1])


# --- PART 1 ---
severity = 0

for i in range(max(layers.iterkeys())+1):
    if not i in layers:
        continue

    depth = layers[i]

    if i % (2*(depth-1)) == 0:
        severity += i*depth

print severity

# --- PART 2 ---

#layers = {0:3, 1:2, 4:4, 6:4}

def walk_firewall(delay):
    for i in range(max(layers.iterkeys())+1):
        if not i in layers:
            continue

        depth = layers[i]

        if (i+delay) % (2*(depth-1)) == 0:
            return False

    return True

delay = 0
safe_pass = False
while not safe_pass:
    delay += 1
    safe_pass = walk_firewall(delay)

print delay

