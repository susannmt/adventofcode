import numpy as np

divider = 2147483647
Afactor = 16807
Bfactor = 48271

Aprev = 634
Bprev = 301
n = 40000000
m = 5000000

A = np.zeros(n, dtype=int)
B = np.zeros(n, dtype=int)
A[0] = Aprev
B[0] = Bprev

judge = 0

for i in range(1, n):
    A[i] = A[i-1]*Afactor%divider
    B[i] = B[i-1]*Bfactor%divider

    if bin(A[i])[-16:] == bin(B[i])[-16:]:
        judge += 1


print judge
