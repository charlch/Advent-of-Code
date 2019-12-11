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
     a= math.atan2(p2[0]-p1[0], p1[1]-p2[1])
     if a<0:
         a+=2*math.pi
     return a

def distance(p1,p2):
    return (p2[0]-p1[0])**2+(p1[1]-p2[1])**2
    



data = list_of_ast(data)


point = (11,13)
angles = []
for other in data:
    if point == other:
        continue
    a = get_angle(point,other)
    d = distance(point,other)
    angles.append((a,d,other))


sorted_unique_angles = sorted(list(set(a[0] for a in angles)))
print(sorted_unique_angles)
angles = sorted(angles,key=lambda tup: tup[1])

i =0
while True:
    for a in sorted_unique_angles:
        points_at_angle = [p for p in angles if p[0]==a]
        if points_at_angle:
            point_to_remove = points_at_angle[0]
            angles.remove(point_to_remove)
            i+=1
            print(f"removed {i}th element")
            if i==200:
                print(point_to_remove)
                raise Exception()
    

print(angles)
