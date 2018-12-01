import pandas as pd
import numpy as np

sheet = pd.read_csv("input.txt", sep="\t", header=None).as_matrix()

# part 1
print np.sum(np.max(sheet, axis=1) - np.min(sheet, axis=1))

# part 2

res = []
m, n = sheet.shape
for row in sheet:
    found = False
    i = 0
    while not found:
        for j in range(n):
            if i == j:
                continue
            if row[i]%row[j]==0:
                res.append(row[i]/row[j])
                found = True
                break
        i += 1

print sum(res)




