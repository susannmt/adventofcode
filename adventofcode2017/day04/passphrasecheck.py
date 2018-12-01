
phrases = open("input.txt", "r").readlines()


# --- Part 1 ---
M = 0 # valid pass phrases

for phrase in phrases:
    words = phrase.split()
    unique = set(words)
    if len(unique) == len(words):
        M += 1

print M


# --- Part 2 ---
M = 0

for phrase in phrases:
    words = [''.join(sorted(w)) for w in phrase.split()]
    unique = set(words)
    if len(unique) == len(words):
        M += 1

print M
