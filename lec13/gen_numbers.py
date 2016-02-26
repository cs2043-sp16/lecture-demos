import sys
import random as r

# This generator relies on a random-number generator so the results will be different every
# time it runs.This file generator does not support the generation of negative sequences.
#
# Feel free to make changes to DIM_X and DIM_Y.  The larger they are, the more numbers you
# will generate.
#
# Details...choose 2222 x 2222 (~10seconds and 25MB of data)
#
# 777 x 7777 takes mycomputer ~2 min to execute, producing ~300MB of data.

DIM_X = 22 # number of lines
DIM_Y = 22 # number of entries per line



VERSION = sys.version_info[0]
# rg takes place of range / xrange function (mixed python)
if VERSION == 2:
    rg = lambda x : xrange(0,x)
elif VERSION == 3:
    rg = lambda x : range(0,x)
else:
    print("Only python2 and python3 are supported...")
    sys.exit(0)

TOTAL = DIM_X * DIM_Y # DO NOT CHANGE!!!
SAMPLE_MAX=9999

FILE_NAME="numbers.txt"

# write to file
with open(FILE_NAME, 'w') as f:
    for x in rg(DIM_X):
        for y in rg(DIM_Y):
            next_int = r.randint(0,SAMPLE_MAX)
            f.write("%d " % next_int)

        f.write("\n")
