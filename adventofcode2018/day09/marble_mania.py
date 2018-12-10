import numpy

N = 446    # number of players
n = 71522  # number of marbles

scores = numpy.zeros(N)
circle = [0]
i = 0
for marble in range(1, n*100):
    if marble % 23 == 0:
        player = marble % N
        scores[player] += marble
        i -= 7
        while i < 0:
            i = len(circle) + i
        scores[player] += circle.pop(i)
    else:
        i += 2
        if i > len(circle):
            i = i - len(circle)
        circle.insert(i, marble)

print(max(scores))
