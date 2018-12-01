import numpy as np

divider = 2147483647
Afactor = 16807
Bfactor = 48271

Aprev = 634
Bprev = 301
n = 5000000

#Aprev = 65
#Bprev = 8921

A = [Aprev]
B = [Bprev]

judge = 0

Acompare = []
Bcompare = []

while len(Acompare) < n or len(Bcompare) < n:
    A.append(A[-1]*Afactor%divider)
    B.append(B[-1]*Bfactor%divider)


    if A[-1] % 4 == 0:
        Acompare.append(A[-1])

    if B[-1] % 8 == 0:
        Bcompare.append(B[-1])


for a,b in zip(Acompare[:n], Bcompare[:n]):
    if bin(a)[-16:] == bin(b)[-16:]:
        judge += 1

print judge

