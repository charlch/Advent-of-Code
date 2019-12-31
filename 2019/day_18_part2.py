from string import ascii_lowercase, ascii_uppercase
from collections import deque



data = """#################################################################################
#...........#.............#...#.....#...#...............#.....#.....#....t#.....#
#.#####.###.###.#########.#.#.#.#.###.#.#.#####.#######.#.###.#.###.#.###.#.#.#.#
#..m#.#...#...#...#...#...#.#...#.....#.#.....#...#...#...#...#...#...#...#.#.#.#
###.#.###.###.###.###.#.#######.#######.#######.#.#.#.#####.#####.#####.###.#.#.#
#.#...#...#.#...#...#.#.#.....#.#.......#.....#.#...#.....#.#...#...#.#...#.#.#.#
#.###.#.###.###.###.#.#.#.###.#.#.#####.#.###.###########.#.#.#.###.#.###.#.#.#.#
#.#...#.#.....#.....#.#...#.#.#.#.#.#...#...#...B.........#...#.J.#.#...#.#.#.#.#
#.#.###.###.#########.#####.#.###.#.#.#####.#####################.#.###.#.###.#.#
#.#...#.#...#.........#...#.#...#.#.#.#.#...#.............#...#...#.#...#....v#.#
#.###.#.#.###.#####.#.#.#.#.###.#.#.#.#.#.###.###########.#.#.#.###.#.#########P#
#.#...#.#.....#.#...#...#.#...#...#.#.#.#...#.....#...#...#.#...#w..#.#...#.....#
#V#.###.#.#####.#.#######.#.#.#####.#.#.#.#.#####.#.#.#.###.#####.###.#.#.#.#####
#...#...#.....#.#.#.......#.#.......#.#.#.#.#.....#.#.#.#.#.#...#.#...#.#.#.....#
#####.#######.#.#.#######.###.#####.#.#.#.#.#.#####.#.#.#.#.###.#.#.###.#.#####.#
#...#...#.......#.......#.....#.....#.#.#.#.#...#...#.....#.....#.#.#...#...#...#
#.#.###.###.#######.###.#######.#####.#.#.#N#.#.#########.###.###.#.#.###.###.###
#.#...#...#.#.....#...#.#...#.#.....#...#.#.#.#...#.....#.#...#...#...#.#...#.#.#
#.###.###.###.###.###.#.#.#.#.###.#####.###.#.###.#.###.###.###.###.###D###.#.#.#
#.#.......#...#.#...#.#...#.#.....#...#.#...#.#...#...#.#...#...#.#.#.....#.#...#
#.#######.#.###.###.###.###.#######.#.#.#.###.#.#####.#.#.###.###.#.#.###.#.###.#
#.T.#.....#.#.....#...#...#.........#...#.#...#.....#.#.....#.#...#.#.#...#.....#
###.#.#####.#.#.#########.###############.#########.#.###########.#.#.###########
#.#.#...#...#.#.........#...#.........#.#...#.....#.....#.........#.#...........#
#.#.#####.###.#####.#######.#######.#.#.###.#.###.#######.#####.###.#####.#######
#.#......l#.#.....#.......#.........#...#...#.#.#.#.....#...#.#...#.....#...#...#
#.#########.#.#########.#.#############.#.###.#.#.#.###.###.#.###.#####.#.#.#.#.#
#.....#.....#.#...#...#.#...#.......#..z#.....#.#...#.....#.#...#.......#.#...#.#
#.###.#.###.#.#.#.#.#.###.#.#.###.#.#.###.#####.#####.#####.#.#.#########.#####.#
#...#.#.#.#...#.#.#.#...#.#.#.#...#.#...#.#.........#.....#...#.#...#.....#.....#
###.###.#.#####.#.#.###.#.#.###.#.#####.#.#######.#.#####.#####.#.#.#.#####.###.#
#...#..d#.#...#.#.#...#...#...#.#.#.....#.....#...#.....#.....#...#.#...#q..#.#.#
#.#.#.###.#.#.#.#.###.#######.#.#.#.#########.#.###########.#.#####.#####.###.#.#
#.#.#...#.#.#...#.#...#.........#.#.#...#.#...#...........#.#.....#...#...#...#.#
#.#####.#.#.#####.#.#######.#######.#.###.#.###.#########.#.#####.###.#.#####.#.#
#.......#.#...#...#.#.....#.#.......#...#.#.#.....#.....#.#...#...#...#.....#...#
#.#######.###.###.#.#.###.###.#######.#.#.#.#####.#.#####.###.#####.#######.#####
#.......#...#...#...#.#.#...#.#...#...#.#.#.#...#...#...#...#.....#.#.....#.....#
#######.#.#.###.#####.#.###.#.#.#.#####.#.#.#.#.#####.#.###.#####.#.#.###.#####.#
#.........#...#...........#.....#......@#@....#....c..#.........#.....#.........#
#################################################################################
#...........#.........#.C.........#....@#@....#.........#.....................X.#
#Q#########.#.#.#####.#.#########.#.###.#.###.#.#######.#.###############.#####.#
#.#.........#.#...#.#...#.......#.#.#.#.#...#.....#...#.#.....#.#.......#...#...#
#.#####.#########.#.#####.#####.#.#.#.#.###.#######.#.#.#####.#.#.#####.#.###.#.#
#.....#.#.....#...#.....#.#...#.#...#.#.#.#.#...#...#...#.....#.#.#.....#.#u..#.#
#.###.#U#.###.#.#####.###.#.###.#####.#.#.#.###.#.#.#####.#####.#.#.#######.###.#
#j..#.#...#...#.....#.#...#...#.....#.#.#.#.....#.#.#.....#.....#.#.........#...#
###.#.#####.#######.#.#.#####.###.#.#.#.#.#####.#.###.#####.###.#.#####.#######.#
#...#.....#.....#...#.#...#...#...#.#.#.#...#...#.....#.....#...#.#...#.#.....#.#
#######.#.#####.#.###.###.#.#.#.###.#.#.###.#.#########.#####.###.#.#.###.###.###
#.....#.#...#.#.#.#.....#.#.#.#.#.....#.#...#.#.....#...#.....#.#...#.......#...#
#.###.#.###.#.#.#.###.#.#.#.#.#.#######.#.###.###.#.###.#.#####.###########.###.#
#f#.#.#.#...#.#.#...#.#.#b#.#.#.#.......#.#...#...#.#...#.....#...#.....#...#...#
#.#.#.###.###.#.###.#.#.#.#.###.#.#######.#.###.###.#.#######.###.#.###.#####.#.#
#.#.......#...#.#...#.#...#...#...#.....#...#...#.....#...........#.#.#.#.....#.#
#.#########.#.#.#.###.#######.#######.###.###.#.#######.###########.#.#.#.#####.#
#.....#.....#.....#....x....#.......#...#n#...#.#.....#.....#.....#.#.#.F.#...#.#
#.###.#####.###############.###.###.###.#.###.###.###.#######.###.#.#.#####.###.#
#...#.....#.#r..........#.#.....#.#...#.#.....#...#...........#...#.#.#.........#
#.#######.###.#########R#.#######.###.#.#####.#.###.###########.###K#.#.#########
#.#.......#...#....g#...#.........#...#.#.....#.#...#.......#.#.....#.#...#.....#
#.#.#######.#######.#####.#.#######.###.#.#####.#.###.#####.#.#######.###.#.#.###
#.#...#...#...#.....#.....#.......#...#.#...#.#.#.#...#...#.#.#.#...#.....#.#...#
#.###.#.#.###G#.###I#.###########.###.#.###.#.#.#.#.#####.#.#.#.#.#.#.#####.###.#
#k#...#.#...#...#...#.....#s....#.#...#.#...#.#.#.#.......#...#...#.#.#.#...#.L.#
###.#.#.###.#####.#######.#.###O#.#.###.#.###.#.#.#######.#####.###.#.#.#.###.#.#
#..p#.#...#.....#.......#.#.#...#.#.....#.Z...#.#...#...#.#...#.#.#...#.#...#.#.#
#.###.###.###.#########.###.#.###.#####.#######.###.###.#.#.#.#.#.#####.###.#.###
#.#.#...#...#.......#..i#...#...#.#.....#.....#.#.#.....#.#.#...#....a....#.#...#
#.#.###.#.#######.#.#H###.#####.#.#.#####.###.#.#.#.#####.#.#####.#.#######.###.#
#.#.....#.#.....#.#.#.#...#o....#.#.#...#...#...#...#.....#.#...E.#.#......y..#.#
#.#######.#.###.###.#.#S#####.###.#.###.#.#.###.#####W#####.#.#.###.#.#########.#
#.#.......#.#.......#.#.....#.A.#.....#.#.#.#...#...#...#...#.#.#...#.#...#.....#
#.#.#######.#######.#.#####.###.#####.#.###.#.###.#.###.#.###.#.#####.###.#.###.#
#.#...#...#.#.Y.#...#..h....#.#...#.#.#.#...#...#.#.....#.#...#...........#...#.#
#.###.#.#.#.#.#.#############.###.#.#.#.#.###.###.#######.#############.#####.#.#
#...#...#.#...#...........#.......#.#.#.#.#...#...#.....#...#.........#.#.....#.#
#.#.#####.###########.#####.#######.#.#.#.#####.###.#######.#.#######.###.#####.#
#.#.....M...........#e......#...........#.......#.............#...........#.....#
#################################################################################"""


_data="""
#########
#BA@#@a##
#c#######
#####@b##
#########
"""
bd = {}
keys = {}
doors = {}
locs = []
for y, line in enumerate(data.split("\n")):
    for x, char in enumerate(line):
        if char!="#":
            bd[(x,y)] = char
        if char in ascii_lowercase:
            keys[char]=(x,y)
        if char in ascii_uppercase:
            doors[char]=(x,y)
        if char == "@":
            bd[(x,y)] = '.'
            locs.append((x,y))
all_keys = set(keys.keys())
print(all_keys)
UP=(0,-1);DO=(0,1);LE=(-1,0);RI=(1,0)
directions = (UP,DO,LE,RI)

def add(a,b):
    return (a[0]+b[0], a[1]+b[1])


best = 1e9
q= deque()
q.append((tuple(locs), frozenset(), 0))
seen={}
while q:
    
    point = q.popleft()

    point_locs=point[0]
    seen_keys = point[1]
    distance = point[2]

    point_key = (tuple(point_locs), frozenset(seen_keys))
    if point_key in seen and distance>=seen[point_key]:
        continue
    seen[point_key] = distance

    
    new_seen_keys = set(seen_keys)
    
    bad=False
    for point_loc in point_locs:
        if point_loc not in bd: #not a real location
            bad=True
            break

        if bd[point_loc] in doors and bd[point_loc].lower() not in seen_keys: # a door we dont have
            bad=True
            break
    
    if bad:
        continue

    D = {}
    q2 = deque()
    for i,point_loc in enumerate(point_locs):
        q2.append((point_loc, i,0))
    while q2:
        point_loc, i, d = q2.popleft()
        if point_loc not in bd:
            continue
        if bd[point_loc] in doors and bd[point_loc].lower() not in seen_keys:
            continue
        if point_loc in D:
            continue
        D[point_loc] = (d,i)
        for di in directions:
            q2.append((add(point_loc, di), i, d+1))

    for key, key_loc in keys.items():
        if key not in seen_keys and key_loc in D:
            d, i = D[key_loc]
            new_locs = list(point_locs)
            new_locs[i] = key_loc
            new_keys = set(seen_keys)
            new_keys.add(key)
            new_dist = d+distance
            if len(new_keys)==len(all_keys):
                if new_dist<best:
                    best=new_dist
                    print(best)
            q.append((tuple(new_locs) ,frozenset(new_keys),new_dist))
            
