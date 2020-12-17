from utils import *
from collections import defaultdict
data = """.#.
..#
###"""
data="""..##.##.
#.#..###
##.#.#.#
#.#.##.#
###..#..
.#.#..##
#.##.###
#.#..##."""
grid = {}

for y,lin in enumerate(data.split("\n")):
    for x,char in enumerate(lin):
        if char=="#":
            grid[(x,y,0,0)] = True

def printgrid(gd, z,w):
    x_range = range(-50,50)
    y_range   = range(-50,50)
    rep = "┌" + ("".join(str(i%10) for i in x_range)) + "x\n"
    for y in y_range:
        rep+=str(y%10)+"".join("#"if gd.get((x,y,z,w))else " " for x in x_range)+"│\n"
    rep += "y" + ("─"*len(x_range)) + "┘\n"
    print(rep)


printgrid(grid,0,0)
for loop in range(0,6):
    n_count = defaultdict(int)
    for p in grid:
        for i in (-1,0,1):
            for j in (-1,0,1):
                for k in (-1,0,1):
                    for w in (-1,0,1):
                        if i==j==k==w==0:
                            continue
                        n_count[(p[0]+i,p[1]+j,p[2]+k,p[3]+w)] +=1

    new_grid = {}
    for p,ns in n_count.items():
        if ns == 3:
            new_grid[p] = True
        if ns ==2 and grid.get(p):
            new_grid[p] = True

    grid = new_grid
    printgrid(grid,0,0)



print(len(grid))
        
                    

                


    
