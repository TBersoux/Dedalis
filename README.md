# Dedalis
A little maze generator made to train my algorithm skills.

Only a single path go from one cell to another. It's also true for the enter and the exit. ("Perfect maze")

To compile, use qmake and make then execute the compiled code. A 300x300 or smaller maze should generate iin less than a min.

The maze generation is not optimal at all, as I didn't look for any existing algorithm and just wanted to create my own.

After looking at existing algorithm, mine looks like the "Randomized Kruskal's algorithm", but sub-optimal as I didn't use disjoint set data structure.
