from knothash import get_hash
import numpy as np
from scipy.ndimage import label

key = 'jxqlasbh'
#key = 'flqrgnkx'

n = 128
s = 0
rows = []
for i in range(n):
    hashcode = get_hash("%s-%d" %(key, i))
    row = ""
    for i in range(16):
        h = int(hashcode[2*i:2*(i+1)], 16)
        b = bin(h)
        row += "%08d" %int(b[2:])
    rows.append(np.array(list(row)))
    s += row.count('1')

print s

# --- PART 2 ---
matrix = np.vstack(rows).astype(int)
regions, num_regions = label(matrix)
print num_regions




