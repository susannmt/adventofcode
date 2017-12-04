import math
import numpy as np


query = 312051
#query = 1024

# find size of spiral
dim = math.ceil(math.sqrt(query))
if dim % 2 == 0:
    dim += 1

mid = math.floor(dim/2.)
from_centre = math.floor(dim/2.)


# distance from lower right corner
dis = dim ** 2 - query
if dis < dim-1:       # south
    steps = abs(dis-mid) + from_centre
elif dis < 2*(dim-1):   # west
    steps = abs((dis-(dim-1)) - mid) + from_centre
elif dis < 3*dim:   # north
    steps = abs((dis-2*(dim-1)) - mid) + from_centre
elif dis < 4*dim:
    steps = abs((dis-3*(dim-1)) - mid) + from_centre

print steps

# --- PART 2 ---
matrix = np.zeros([dim, dim])
matrix[mid, mid] = 1

W, E, S, N = (0, -1), (0, 1), (1, 0), (-1, 0)
left = {N: W, W: S, S: E, E: N}

def get_val(m, i, j):
    s = m[i,j-1] + m[i,j+1] + m[i+1,j] + m[i-1,j]
    s+= m[i-1, j-1] + m[i-1, j+1] + m[i+1, j-1] + m[i+1, j+1]
    return s
i, j = mid, mid
i_dir, j_dir = S

while matrix[i,j] < query:
    # trying to turn left
    new_i_dir, new_j_dir = left[i_dir, j_dir]
    new_i, new_j = i+new_i_dir, j+new_j_dir

    if (0 <= new_i < dim and 0 <= new_j <= dim 
            and matrix[new_i, new_j] == 0):
        i, j = new_i, new_j
        i_dir, j_dir = new_i_dir, new_j_dir
        matrix[i, j] = get_val(matrix, i, j)

    # allready something stored left
    else:
        i, j = i + i_dir, j + j_dir
        matrix[i, j] = get_val(matrix, i, j)

print matrix[i,j]
