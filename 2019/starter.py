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
# product('ABCD', repeat=2)                   AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)                     AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)                     AB AC AD BC BD CD
# combinations_with_replacement('ABCD', 2)    AA AB AC AD BB BC BD CC CD DD

from computer import Process

prog= [109,424,203,1,21101,11,0,0,1105,1,282,21102,18,1,0,1106,0,259,1201,1,0,221,203,1,21102,1,31,0,1105,1,282,21101,38,0,0,1106,0,259,20102,1,23,2,21201,1,0,3,21101,1,0,1,21102,57,1,0,1105,1,303,1201,1,0,222,21001,221,0,3,20101,0,221,2,21102,1,259,1,21101,0,80,0,1105,1,225,21101,76,0,2,21102,1,91,0,1106,0,303,2102,1,1,223,21002,222,1,4,21102,1,259,3,21101,0,225,2,21102,225,1,1,21102,1,118,0,1105,1,225,21001,222,0,3,21102,1,54,2,21102,1,133,0,1106,0,303,21202,1,-1,1,22001,223,1,1,21101,148,0,0,1106,0,259,1202,1,1,223,21001,221,0,4,20101,0,222,3,21101,14,0,2,1001,132,-2,224,1002,224,2,224,1001,224,3,224,1002,132,-1,132,1,224,132,224,21001,224,1,1,21101,0,195,0,106,0,108,20207,1,223,2,20101,0,23,1,21101,0,-1,3,21102,1,214,0,1105,1,303,22101,1,1,1,204,1,99,0,0,0,0,109,5,1202,-4,1,249,22102,1,-3,1,21201,-2,0,2,21202,-1,1,3,21101,0,250,0,1106,0,225,22101,0,1,-4,109,-5,2105,1,0,109,3,22107,0,-2,-1,21202,-1,2,-1,21201,-1,-1,-1,22202,-1,-2,-2,109,-3,2105,1,0,109,3,21207,-2,0,-1,1206,-1,294,104,0,99,21201,-2,0,-2,109,-3,2105,1,0,109,5,22207,-3,-4,-1,1206,-1,346,22201,-4,-3,-4,21202,-3,-1,-1,22201,-4,-1,2,21202,2,-1,-1,22201,-4,-1,1,22101,0,-2,3,21102,1,343,0,1106,0,303,1106,0,415,22207,-2,-3,-1,1206,-1,387,22201,-3,-2,-3,21202,-2,-1,-1,22201,-3,-1,3,21202,3,-1,-1,22201,-3,-1,2,22102,1,-4,1,21101,0,384,0,1105,1,303,1106,0,415,21202,-4,-1,-4,22201,-4,-3,-4,22202,-3,-2,-2,22202,-2,-4,-4,22202,-3,-2,-3,21202,-4,-1,-2,22201,-3,-2,1,21202,1,1,-4,109,-5,2106,0,0]


def add(a,b):
    return (a[0]+b[0],a[1]+b[1])


RIGHT=(1,0)
DOWN = (0,1)

def main():
    count=0
    for y in range(20):
        s=""
        for x in range(20):
            p = Process(prog)
            l = p.run(inpt=[x,y]).output[-1]
            count+=l
            s+=str(l)
        print(s)
    print(count)

def is_in(point):
    return Process(prog).run(inpt=list(point)).output[-1] == 1

def main2():
    #Idea edge find along each edge, keeping points at 45 degrees

    tp = (10,0)
    bp = (0,10)
    #Firstly move to find the edge
    while True:
        tp = add(tp, DOWN)
        if is_in(tp):
            break
    while True:
        bp = add(bp, RIGHT)
        if is_in(bp):
            break

    while True:
        #Three options:
            # 1. Already at 45deg, must check block size and then move one of them
            # 2. tp is behind, move it
            # 3. bp is behind, move it
        #print(tp,bp, sum(tp),sum(bp))
        if sum(tp)==sum(bp):
            if (tp[0]-bp[0]>=99) and (bp[1] - tp[1]>=99):
                print(tp,bp)
                print(bp[0]*10000+tp[1])
                break
        if sum(tp)>=sum(bp):
            #move bp
            bp=add(bp, DOWN)
            while not is_in(bp):
                bp=add(bp,RIGHT)
            
        else:
            #move tp
            tp=add(tp, RIGHT)
            while not is_in(tp):
                tp=add(tp,DOWN)
    
if __name__ == "__main__":
    main()
    main2()

