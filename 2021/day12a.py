from collections import defaultdict
data = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

_data = """start-a
a-b
b-c
c-end"""
_data="""fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""
data="""cz-end
cz-WR
TD-end
TD-cz
start-UM
end-pz
kb-UM
mj-UM
cz-kb
WR-start
WR-pz
kb-WR
TD-kb
mj-kb
TD-pz
UM-pz
kb-start
pz-mj
WX-cz
sp-WR
mj-WR"""
paths = defaultdict(set)

for line in data.split("\n"):
    f,t = line.split("-")

    if t not in ("start"):
        paths[f].add(t)

    if f not in ("start"):
        paths[t].add(f)

small_caves = set()
for k in paths.keys():
    if k.lower() ==k:
        small_caves.add(k)

#print(small_caves)    

def path_finder(path_so_far, location, dobule_vis=False, d=1):
    #print("."*d, path_so_far, location)
    if location =="end":
        return [path_so_far]

    ps = []
    
    for op in paths[location]:
        
        if op in small_caves and op in path_so_far:
            if dobule_vis:
                continue
            else:
                dv=True
        else:
            dv = dobule_vis
        ps+=path_finder(path_so_far+[op], op, dv, d+1)
    return ps

a= path_finder([],"start")
#print(a)
print(len(a))
        
    
