#!/usr/bin/env python3

# A simple program to debug!
#
# You need to have ipdb installed...`pip3 install ipdb`
import ipdb

# Create a small matrix just for fun.
N = 5
mat = [[x for x in range(N)] for y in range(N)]

# Print the matrix before:
print("Before transpose:")
for row in mat:
    print(row)

# A simple transpose?
#
# Run the program once and you will see that it is not performing
# the transpose we expect!
#
# Now lets debug it with our shiny new python toy.
#
# Un-comment the line below to start the trace.
# ipdb.set_trace()
#
# This is just like gdb!  Type 'h' to see the commands.
#
# Type exit() to leave the debugger.
#
# E.g.
#
# s           <<< step one line of code, enter the outer loop
# p x         <<< print value of x
# s           <<< step into inner loop
# p y         <<< print value of y
# s           <<< Skipping (0,0) because it is pointless
# s           <<< Skipping (0,0) because it is pointless
# s           <<< Skipping (0,0) because it is pointless
# p x         <<< 0
# p y         <<< 1
#
# [[[ we are now debugging the swap of (0,1) with (1,0) ]]]
# [[[ lets examine the values before we make the switch ]]]
#
# p mat[x][y] <<< Gives us 1
# p mat[y][x] <<< Gives us 0
#
# [[[ lets execute the two instructions now with two s  ]]]
#
# s           <<< Execute first swap
# s           <<< Execute second swap
#
# [[[ print the values to make sure they got swapped    ]]]
# [[[ note: use up arrow to scroll through your history ]]]
#
# p x         <<< Make sure we are still at the right indices.
# p y
#
# p mat[x][y] <<< Gives us 0, seems good so far
# p mat[y][x] <<< Gives us 0...WHOOPS!  We need a tmp variable
#
# exit()      <<< Quit the debugger.
#
for x in range(N):
    for y in range(N):
        mat[x][y] = mat[y][x]
        mat[y][x] = mat[x][y]

# Print the results.
print("------------------")
print("After transpose:")
for row in mat:
    print(row)
