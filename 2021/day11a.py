from utils import *
data= """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""
_data = """11111
19991
19191
19991
11111"""
data="""5651341452
1381541252
1878435224
6814831535
3883547383
6473548464
1885833658
3732584752
1881546128
5121717776"""

def step(b):
    #First, the energy level of each octopus increases by 1.
    for k,v in b.items():
        b[k]=v+1

    flashed = set()
    
    while True:
        to_flash = set()
        for k,v in b.items():
            if v>9:
                to_flash.add(k)

        to_flash = to_flash - flashed
        for p in to_flash:
            for d in DIRS_8:
                if p+d in b:
                    b[p+d]+=1

        flashed = flashed | to_flash

        if not to_flash:
            break

    for p in flashed:
        b[p]=0

    return len(flashed)


b = Board(data)
b = {k:int(v) for k,v in b.items()}
fls = 0
for _ in range(100):
    fls +=step(b)
print(fls)


b = Board(data)
b = {k:int(v) for k,v in b.items()}
c=1
while step(b)<100:
    c+=1
print(c)
    
