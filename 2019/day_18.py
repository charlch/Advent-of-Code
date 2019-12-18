import os  # NOQA
import sys  # NOQA
import re  # NOQA
import math  # NOQA
import time
import fileinput
from string import ascii_uppercase, ascii_lowercase  # NOQA
from collections import Counter, defaultdict, deque, namedtuple  # NOQA
from itertools import count, product, permutations, combinations, combinations_with_replacement  # NOQA
import random
from utils import parse_line, parse_nums, mul, all_unique, factors, memoize, primes  # NOQA
from utils import new_table, transposed, rotated  # NOQA
from utils import md5, sha256, knot_hash  # NOQA
from utils import VOWELS, CONSONANTS  # NOQA
from utils import Point, DIRS, DIRS_4, DIRS_8,chunks  # NOQA

# Itertools Functions:
# product('ABCD', repeat=2)                   AA AB AC AD BA BB BC mbd CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)                     AB AC AD BA BC mbd CA CB CD DA DB DC
# combinations('ABCD', 2)                     AB AC AD BC mbd CD
# combinations_with_replacement('ABCD', 2)    AA AB AC AD BB BC mbd CC CD DD

from computer import Process



data="""#########
#b.A.@.a#
#########"""

data="""#################################################################################
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
#.........#...#...........#.....#.............#....c..#.........#.....#.........#
#######################################.@.#######################################
#...........#.........#.C.........#...........#.........#.....................X.#
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

mbd = {}
keys = {}
doors = {}
rob =None
for y,line in enumerate(data.split("\n")):
    for x,char in enumerate(line):
        if char!="#":
            pos=(x,y)
            mbd[pos]=char
            if char in ascii_uppercase:
                doors[char]=pos
            if char in ascii_lowercase:
                keys[char]=pos
            if char == "@":
                rob=pos

print(mbd)
print(keys)
print(doors)
print(rob)


def  printbd(bd):
    for y in range(2):
        print("".join(bd.get((x,y)," ") for x in range(10)))

def add(a,b):
    return (a[0]+b[0],a[1]+b[1])

UP=(0,-1)
RI=(1,0)
LE =(-1,0)
DO = (0,1)

def dostuff(bd, loc, total_so_far):
    #printbd(bd)
    #print( loc, total_so_far)
    count_bd ={}
    count_bd[loc]=0

    to_look_at = [add(loc,o) for o in (UP,RI,LE,DO)]
    keys_hit=[]
    doors_left = False
    while len(to_look_at)>0:
        point = to_look_at.pop(0)
        #print(point)
        if point in count_bd:
            continue
        if point not in bd:
            continue
            
        v = min(count_bd.get(add(point,o),100000) for o in (UP,RI,LE,DO))
        if v==100000:
            to_look_at.append(point)
            continue
        
        if bd.get(point)!=".":
            #key or door?
            if bd.get(point) in keys:
                keys_hit.append((point, bd.get(point), v+1))
                continue
            if bd.get(point) in doors:
                doors_left=True
                continue
            
    
        count_bd[point]=v+1
        to_look_at.extend(add(point,o) for o in (UP,RI,LE,DO))

    if not doors_left and len(keys_hit)==0:
        print("Yay")
        return total_so_far

    if doors_left and len(keys_hit)==0:
        return None

    trials=[]
    for point, key, dist in keys_hit:
        new_bd = bd.copy()
        new_bd[point]="."
        if key.upper() in doors:
            new_bd[doors[key.upper()]]="."
        trials.append(dostuff(new_bd,point,dist))

    trials = [t for t in trials if t!=None]
    if trials:
       
        return total_so_far + min(trials)
    return None
        
        
        
                

print("-"*25)
print(dostuff(mbd,rob, 0))
            
    
    


