import math
from collections import defaultdict
from time import sleep
data = """10 ORE => 10 A
1 ORE => 1 B
7 A, 1 B => 1 C
7 A, 1 C => 1 D
7 A, 1 D => 1 E
7 A, 1 E => 1 FUEL"""

data = """9 ORE => 2 A
8 ORE => 3 B
7 ORE => 5 C
3 A, 4 B => 1 AB
5 B, 7 C => 1 BC
4 C, 1 A => 1 CA
2 AB, 3 BC, 4 CA => 1 FUEL"""

data="""157 ORE => 5 NZVS
165 ORE => 6 DCFZ
44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
179 ORE => 7 PSHF
177 ORE => 5 HKGWZ
7 DCFZ, 7 PSHF => 2 XJWVT
165 ORE => 2 GPVTF
3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT"""

data = """15 RNMTG => 6 QSXV
21 MKJN => 9 KDFZ
1 KVFL, 4 NZWL => 3 FHDT
1 FZJXD, 2 SWZK, 1 QRLRS => 6 ZRNK
8 KVFL => 6 SBZKF
11 DXFB, 1 CPBXJ, 8 TXFCS, 1 ZPMHL, 1 BCHTD, 2 FZJXD, 2 WKZMQ, 1 NZWL => 8 MPLJ
5 KDFZ, 1 QSXV => 9 TXFCS
1 PMLGM, 21 CKVN => 3 KVFL
1 XFRLH, 3 QRLRS => 4 CKVN
5 KBJS, 15 XFRLH, 6 WZPZX, 15 KVFL, 4 DXFB, 4 ZPMHL, 11 JCKCK, 26 KFGPB => 9 BWVS
10 KNRDW, 2 XCML => 9 BCNL
26 LBLH => 9 KBJS
5 DTFBQ, 4 PJTD => 6 FHKSW
6 HTRFP, 1 FVXV, 4 JKLNF, 1 TXFCS, 2 PXBP => 4 JRBFT
21 DTFBQ => 9 JGQJ
2 KBJS => 3 FZJXD
24 LBLH => 6 QFMTZ
1 CBNJT => 7 LSCW
5 KVFL => 2 NZWL
12 DNHL, 4 BCNL => 4 LBLH
15 RHVG => 1 PJCWT
4 KDFZ, 1 KVFL => 3 BCHTD
2 XFDW, 7 BCHTD => 7 WKZMQ
2 SBZKF, 1 PLTX => 3 DXFB
1 PLTX, 11 HTRFP, 6 PMLGM => 1 JCKCK
1 TQCX, 10 DNHL => 8 DTFBQ
2 TQCX, 2 KTBFB => 5 RHVG
8 MVFW => 3 CPBXJ
148 ORE => 4 CBNJT
9 CPBXJ, 5 DTFBQ => 6 PMLGM
11 ZXCF, 15 PJCWT, 4 FZJXD => 7 PJTD
1 JGQJ => 6 DCBNV
4 LSCW, 16 BCNL => 7 MVFW
1 RHVG => 4 XFDW
8 MPLJ, 16 JRBFT, 43 KBJS, 11 NZWL, 4 BWVS, 22 ZPMHL => 1 FUEL
1 QFMTZ, 3 CKVN => 5 PLTX
5 CKVN, 10 SWZK => 7 HTRFP
2 PXBP, 1 QRLRS, 7 KTBFB => 7 NDZGV
1 QRLRS, 9 KBJS, 2 TQCX => 2 SWZK
9 TZKZ, 3 ZRNK, 4 PXBP => 4 FVXV
1 PMLGM, 1 SWZK, 6 FZJXD => 7 MKJN
16 MVFW, 2 KBJS => 7 ZXCF
1 MVFW => 6 HVGF
1 LSCW, 1 HVGF => 8 RNMTG
5 ZRNK, 1 TQCX => 3 PXBP
130 ORE => 5 KNRDW
1 RHVG, 2 KFGPB, 1 LSCW => 7 QRLRS
6 XFRLH => 8 TZKZ
24 HVGF, 8 KTBFB => 1 XFRLH
2 KNRDW, 2 CBNJT => 6 DNHL
1 FHDT => 4 JKLNF
1 QSXV, 10 XFGZX, 2 DCBNV => 8 ZPMHL
1 FHDT, 7 NDZGV => 4 WZPZX
11 FHKSW => 5 XFGZX
10 LSCW => 8 KTBFB
133 ORE => 1 XCML
8 XCML => 4 TQCX
6 CPBXJ, 8 CBNJT => 6 KFGPB"""
stuff = {}
for row in data.split("\n"):
    a,b = row.split("=>")
    c = a.split(",")
    e= b.strip().split(" ")
    stuff[e[1]]=[int(e[0])]
    for d in c:
        q, chem = d.strip().split(" ")
        stuff[e[1]].append([int(q),chem])



def can_make(fuel):
    needed = defaultdict(int)
    needed['FUEL']=fuel
    ore_need=0
    #print(stuff)
    while True:
        keys = list(needed.keys())
        for key in keys:
            #print(needed)
            if key =='ORE':
                continue
            needed_quantity = needed[key]
            if needed_quantity>0:
               made_qty, *parts = stuff[key]
               multi = math.ceil(needed_quantity/made_qty)
               needed[key] -= multi*made_qty
               for part in parts:
                   needed[part[1]]+=multi*part[0]
        if [k for k,v in needed.items() if v>0]==['ORE']:
            break

    return needed['ORE']<1000000000000


s=460664
e=5586022
assert can_make(s)
assert not can_make(e)
while e-s>1:
    p= (e+s)//2
    if  can_make(p):
        s=p
    else:
        e=p
print(s)
