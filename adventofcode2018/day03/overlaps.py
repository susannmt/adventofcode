import numpy

with open("input.txt", "r") as input_file:
    claims = input_file.readlines()

fabric = numpy.zeros((1000,1000))
for claim in claims:
    claim = claim.split()
    x, y = [int(c) for c in claim[2].strip(':').split(',')]
    w, h = [int(c) for c in claim[3].split('x')]

    fabric[y:y+h, x:x+w] += 1

overlaps = fabric != 0
overlaps &= fabric != 1
print(numpy.count_nonzero(overlaps))

for claim in claims:
    claim = claim.split()
    claim_nr = int(claim[0][1:])
    x, y = [int(c) for c in claim[2].strip(':').split(',')]
    w, h = [int(c) for c in claim[3].split('x')]

    if numpy.all(fabric[y:y+h, x:x+w] == 1):
        print(claim_nr)
        break
