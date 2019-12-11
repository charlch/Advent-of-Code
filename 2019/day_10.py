import math

data = """...###.#########.####
.######.###.###.##...
####.########.#####.#
########.####.##.###.
####..#.####.#.#.##..
#.################.##
..######.##.##.#####.
#.####.#####.###.#.##
#####.#########.#####
#####.##..##..#.#####
##.######....########
.#######.#.#########.
.#.##.#.#.#.##.###.##
######...####.#.#.###
###############.#.###
#.#####.##..###.##.#.
##..##..###.#.#######
#..#..########.#.##..
#.#.######.##.##...##
.#.##.#####.#..#####.
#.#.##########..#.##."""

def list_of_ast(d):
    o=list()
    for r,row in enumerate(d.split()):
        for c,space in enumerate(row):
            if space == "#":
                o.append((c,r))
    return o
            

def get_angle(p1,p2):
     return math.atan2(p1[0]-p2[0], p1[1]-p2[1])
    


data = list_of_ast(data)

all_angles=[]
for point in data:
    angles = set()
    for other in data:
        if point == other:
            continue
        a = get_angle(point,other)
        angles.add(a)
    all_angles.append((point,len(angles)    ))

all_angles.sort(key=lambda tup: tup[1])
print(all_angles[-1])
