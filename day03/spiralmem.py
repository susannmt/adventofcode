import math


query = 312051
#query = 1024

# find size of spiral
dim = math.ceil(math.sqrt(query))
if dim % 2 == 0:
    dim += 1

mid = math.floor(dim/2.)
from_centre = math.floor(dim/2.)


print "dim ", dim
print "mid ", mid

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


print "dis ", dis
print steps



