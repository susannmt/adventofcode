def spin(X, sequence):
    return sequence[-X:] + sequence[:-X]

def exchange(A, B, seq):
    a = seq[A]
    b = seq[B]
    seq[A] = b
    seq[B] = a
    return seq

def partner(A, B, seq):
    a = seq.index(A)
    b = seq.index(B)
    seq[a] = B
    seq[b] = A
    return seq

moves = open("input.txt", "r").read().strip().split(',')
sequence = list('abcdefghijklmnop')
#moves = ["s1", "x3/4", "pe/b"]
#sequence = list('abcde')

for move in moves:
    if move[0] == 's':
        sequence = spin(int(move[1]), sequence)

    else:
        who = move[1:].split('/')

        if move[0] == 'x':
            sequence = exchange(int(who[0]), int(who[1]), sequence)

        elif move[0] == 'p':
            sequence = partner(who[0], who[1], sequence)

print ''.join(sequence), len(sequence)


