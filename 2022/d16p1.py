
from collections import namedtuple
from queue import Queue

from parse import *

data = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""

_data = """Valve VN has flow rate=0; tunnels lead to valves LW, TK
Valve FQ has flow rate=0; tunnels lead to valves AJ, YC
Valve DO has flow rate=0; tunnels lead to valves RV, HJ
Valve MW has flow rate=0; tunnels lead to valves TE, HJ
Valve LT has flow rate=5; tunnels lead to valves KO, SG, KH, HZ, RV
Valve UJ has flow rate=0; tunnels lead to valves FW, DE
Valve IZ has flow rate=0; tunnels lead to valves LU, SX
Valve FE has flow rate=17; tunnels lead to valves WG, WI, LC
Valve KS has flow rate=25; tunnels lead to valves QA, BT
Valve HJ has flow rate=11; tunnels lead to valves MW, CZ, ZE, DO
Valve WI has flow rate=0; tunnels lead to valves WX, FE
Valve EK has flow rate=0; tunnels lead to valves KE, BS
Valve HD has flow rate=0; tunnels lead to valves KH, FW
Valve HZ has flow rate=0; tunnels lead to valves XY, LT
Valve CD has flow rate=0; tunnels lead to valves XD, LU
Valve OZ has flow rate=0; tunnels lead to valves GX, LW
Valve AA has flow rate=0; tunnels lead to valves EP, FU, DV, OU, HC
Valve OU has flow rate=0; tunnels lead to valves VX, AA
Valve XD has flow rate=10; tunnels lead to valves VX, VW, BS, XY, CD
Valve AI has flow rate=0; tunnels lead to valves KE, FW
Valve GX has flow rate=0; tunnels lead to valves OZ, WX
Valve FW has flow rate=8; tunnels lead to valves AI, FU, UJ, TK, HD
Valve KO has flow rate=0; tunnels lead to valves DV, LT
Valve DV has flow rate=0; tunnels lead to valves KO, AA
Valve CZ has flow rate=0; tunnels lead to valves LU, HJ
Valve WG has flow rate=0; tunnels lead to valves KE, FE
Valve WX has flow rate=15; tunnels lead to valves WI, GX
Valve AJ has flow rate=0; tunnels lead to valves FQ, LU
Valve LC has flow rate=0; tunnels lead to valves LW, FE
Valve XX has flow rate=0; tunnels lead to valves LA, VW
Valve RK has flow rate=0; tunnels lead to valves BX, LW
Valve YC has flow rate=22; tunnels lead to valves FQ, QA
Valve KH has flow rate=0; tunnels lead to valves HD, LT
Valve ZE has flow rate=0; tunnels lead to valves HJ, SX
Valve BX has flow rate=0; tunnels lead to valves KE, RK
Valve VS has flow rate=24; tunnel leads to valve UP
Valve SX has flow rate=16; tunnels lead to valves IZ, ZE, LV
Valve RV has flow rate=0; tunnels lead to valves LT, DO
Valve UP has flow rate=0; tunnels lead to valves VS, LW
Valve EP has flow rate=0; tunnels lead to valves AA, AU
Valve VO has flow rate=0; tunnels lead to valves KE, HC
Valve HC has flow rate=0; tunnels lead to valves AA, VO
Valve TE has flow rate=0; tunnels lead to valves LA, MW
Valve LW has flow rate=19; tunnels lead to valves UP, OZ, LC, VN, RK
Valve SG has flow rate=0; tunnels lead to valves OY, LT
Valve BT has flow rate=0; tunnels lead to valves KS, LU
Valve DE has flow rate=0; tunnels lead to valves LA, UJ
Valve BS has flow rate=0; tunnels lead to valves EK, XD
Valve VX has flow rate=0; tunnels lead to valves OU, XD
Valve TK has flow rate=0; tunnels lead to valves VN, FW
Valve HQ has flow rate=14; tunnel leads to valve LV
Valve LU has flow rate=20; tunnels lead to valves CZ, IZ, AJ, BT, CD
Valve LA has flow rate=7; tunnels lead to valves OY, XX, TE, DE, AU
Valve VW has flow rate=0; tunnels lead to valves XD, XX
Valve LV has flow rate=0; tunnels lead to valves SX, HQ
Valve XY has flow rate=0; tunnels lead to valves XD, HZ
Valve OY has flow rate=0; tunnels lead to valves SG, LA
Valve KE has flow rate=12; tunnels lead to valves VO, EK, WG, AI, BX
Valve AU has flow rate=0; tunnels lead to valves LA, EP
Valve QA has flow rate=0; tunnels lead to valves YC, KS
Valve FU has flow rate=0; tunnels lead to valves AA, FW"""


data = parse(data, ["Valve ",Str(2)," has flow rate=",Int(),"; ",Str()," to valve", Str(1),Str()])
print(data)
Cave = namedtuple("Cave", "name rate targets")
caves = {}
for name, rate, _ , _ ,target in data:
    targets = [t.strip() for t in target.split(",")]
    print(name, rate, targets)
    caves[name] = Cave(name, rate, {t:1 for t in targets})

for c in caves.items(): print(c)

for name in list(caves.keys()):
    if name=="AA":
        continue
    cave = caves[name]
    if cave.rate ==0:
        del caves[name]
        for n in list(caves.keys()):
            ncave = caves[n]
            if name in ncave.targets:
                new_targets = {k:v for k,v in ncave.targets.items() if k!=name}
                new_targets.update({k:v+1 for k,v in cave.targets.items() if k in caves and k != ncave.name})
                caves[n] = Cave(ncave.name, ncave.rate, new_targets)

print("and now")
for c in caves.items(): print(c)



print(caves)
State = namedtuple("State", "loc score on_valves been time score_at_loc")

start = State("AA", 0, set(),  set(), 1, {})
to_explore = Queue()
to_explore.put(start)

finished = []
states = []
while not to_explore.empty():
    p = to_explore.get()
    #print(p)
    if p.time == 30:
        finished.append(p)
        continue
    cave = caves[p.loc]
    #try turning on the current room
    if p.loc not in p.on_valves and cave.rate!=0:
        new_score = p.score + (30-p.time)*cave.rate
        on_valves = {p.loc}
        on_valves.update(p.on_valves)
        score_at_loc = {}
        score_at_loc.update(p.score_at_loc)
        score_at_loc[p.loc] = new_score
        ns = State(p.loc, new_score, on_valves, p.been, p.time+1 , score_at_loc)

        states.append(ns)
        to_explore.put(ns)

    #try the other rooms
    for n, t in cave.targets.items():

        if n not in p.score_at_loc or p.score>p.score_at_loc[n]:
            been = {p.loc}
            been.update(p.been)
            score_at_loc = {}
            score_at_loc.update(p.score_at_loc)
            score_at_loc[n] = p.score
            ns = State(n, p.score , p.on_valves, been, p.time + t,  score_at_loc)
            states.append(ns)
            to_explore.put(ns)

#print(finished)
m = max(s.score for s in states)
ms = [s for s in states if s.score==m][0]

print(m)

