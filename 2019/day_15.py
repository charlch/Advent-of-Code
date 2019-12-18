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
prog=[3,1033,1008,1033,1,1032,1005,1032,31,1008,1033,2,1032,1005,1032,58,1008,1033,3,1032,1005,1032,81,1008,1033,4,1032,1005,1032,104,99,1002,1034,1,1039,1002,1036,1,1041,1001,1035,-1,1040,1008,1038,0,1043,102,-1,1043,1032,1,1037,1032,1042,1106,0,124,1001,1034,0,1039,1002,1036,1,1041,1001,1035,1,1040,1008,1038,0,1043,1,1037,1038,1042,1106,0,124,1001,1034,-1,1039,1008,1036,0,1041,1001,1035,0,1040,102,1,1038,1043,1002,1037,1,1042,1106,0,124,1001,1034,1,1039,1008,1036,0,1041,102,1,1035,1040,1001,1038,0,1043,1002,1037,1,1042,1006,1039,217,1006,1040,217,1008,1039,40,1032,1005,1032,217,1008,1040,40,1032,1005,1032,217,1008,1039,5,1032,1006,1032,165,1008,1040,35,1032,1006,1032,165,1102,1,2,1044,1106,0,224,2,1041,1043,1032,1006,1032,179,1102,1,1,1044,1106,0,224,1,1041,1043,1032,1006,1032,217,1,1042,1043,1032,1001,1032,-1,1032,1002,1032,39,1032,1,1032,1039,1032,101,-1,1032,1032,101,252,1032,211,1007,0,38,1044,1106,0,224,1101,0,0,1044,1106,0,224,1006,1044,247,1001,1039,0,1034,1001,1040,0,1035,101,0,1041,1036,102,1,1043,1038,1002,1042,1,1037,4,1044,1106,0,0,4,26,16,55,25,8,4,99,2,21,20,20,56,26,97,81,12,2,4,9,32,7,49,54,5,18,81,16,7,88,4,23,30,66,17,31,27,29,34,26,81,62,27,81,41,84,12,53,90,79,37,22,45,27,17,39,76,1,55,58,44,20,18,57,57,20,76,47,20,44,88,26,43,36,79,12,68,30,19,71,27,21,18,75,18,9,56,29,15,84,8,74,93,1,35,91,39,32,86,9,97,54,4,22,59,13,61,31,19,97,26,82,35,73,23,77,71,59,26,76,78,73,34,85,67,26,1,66,91,79,26,95,5,75,99,29,14,23,26,8,66,97,55,21,25,49,17,99,71,37,62,21,45,46,13,29,30,24,31,63,99,12,12,63,10,64,2,76,3,8,37,94,33,12,47,65,35,65,60,12,88,8,10,49,36,12,14,4,43,82,19,16,51,52,20,17,43,18,33,49,19,93,49,29,86,10,31,92,90,44,26,97,8,63,70,81,28,17,80,23,22,79,56,33,67,61,91,37,4,83,77,16,6,8,33,66,92,46,8,34,23,81,3,93,14,23,72,20,91,16,62,79,7,27,81,10,11,44,65,24,66,77,31,12,53,15,50,84,24,70,29,62,50,5,3,88,13,52,85,42,4,15,39,82,65,18,15,58,37,71,10,13,90,98,29,59,52,3,22,13,59,91,29,23,79,1,7,24,80,79,37,31,77,17,11,64,10,9,8,74,97,6,74,35,73,44,68,29,97,3,45,73,30,28,80,9,48,73,76,7,3,77,83,8,12,41,62,44,10,21,27,74,32,95,73,4,47,71,6,67,17,57,10,67,5,25,74,18,24,57,7,61,66,4,51,14,7,44,29,79,74,11,6,49,75,32,3,98,89,63,5,15,5,74,78,37,7,77,3,13,47,9,33,76,22,47,6,72,12,35,75,39,25,87,83,37,19,91,25,45,22,30,54,83,74,22,71,19,3,3,85,74,37,95,26,67,46,10,12,96,44,50,32,90,3,28,56,24,43,4,1,65,5,9,50,22,44,88,9,48,59,21,24,54,11,35,53,28,7,82,32,24,17,45,88,34,72,95,17,9,39,29,4,55,66,95,22,62,15,71,11,39,51,37,86,49,20,10,63,31,66,59,15,55,93,3,11,28,54,30,41,20,92,7,3,12,54,49,14,33,56,89,21,26,67,20,93,7,64,3,31,60,23,51,36,30,57,20,14,28,88,4,6,69,33,65,98,35,96,80,49,25,68,78,97,30,63,35,73,89,32,64,69,10,68,96,19,89,71,41,32,31,30,90,5,71,20,53,36,51,23,87,19,25,15,34,15,48,19,25,33,14,50,64,11,96,19,34,14,44,33,29,40,16,50,90,22,34,44,17,64,63,18,86,57,29,44,22,98,16,41,20,99,34,14,51,11,4,84,91,66,27,49,6,58,34,95,62,6,45,53,27,72,4,12,40,43,17,41,93,27,30,70,31,47,87,26,64,9,63,59,73,9,11,97,35,56,73,23,58,9,49,13,88,1,87,13,54,21,94,13,69,16,39,2,10,64,13,10,19,96,2,23,1,60,99,47,12,61,37,13,70,24,48,91,7,33,51,10,25,88,33,69,29,98,16,16,60,5,29,44,17,21,41,62,65,8,61,84,27,42,78,72,23,98,16,76,98,77,37,19,49,37,93,83,97,1,63,9,63,27,66,34,74,87,58,3,90,4,48,51,67,32,66,9,56,9,44,1,67,24,49,29,58,20,70,32,73,27,82,0,0,21,21,1,10,1,0,0,0,0,0,0]


def ps(s,p):
    l=""
    for y in range(-20,20):
        
        for x in range(-30,30):
            if p==(x,y):
                l+="D"
            elif (x,y)==(0,0):
                l+="S"
            else:
                l+=s.get((x,y)," ")
        l+="\n"
    print(l)

def get_n(pos,di):
        if di==1:
            n=(pos[0],pos[1]-1)
        elif di==2:
            n=(pos[0],pos[1]+1)
        elif di==3:
            n=(pos[0]-1,pos[1])
        elif di==4:
            n=(pos[0]+1,pos[1])
        return n

def right(di):
    if di==1:
        return 4
    if di==2:
        return 3
    if di ==3:
        return 1
    return 2

def left(di):
    if di==1:
        return 3
    if di==2:
        return 4
    if di ==3:
        return 2
    return 1
def main():
    print("Day *")
    pos=(0,0)
    di = 3
    screen={}
    screen[pos]='.'
    count={}
    count[pos]=0
    p =Process(prog)
    c=0
    while True:
        c+=1
        while True:
            if screen.get(get_n(pos,left(di)))!="#":
                di=left(di)
                break
            if screen.get(get_n(pos,(di)))!="#":

                break
            di=right(di)
            break
        l = p.run([di]).output[-1]
        
        n=get_n(pos,di)
        if l ==0:
            screen[n]="#"
        if (n not in count):
            count[n]=count[pos]+1
        if l==1:
            screen[n]="."
            pos=n
        if l==2:
            screen[n]="O"
            
            ps(screen,pos)
            print("here",count[n])
            print(n)
 
            break

        
        if c%1000==0:
            time.sleep(1)
            ps(screen,pos)

    one_changed=True
    c=-1
    while one_changed:
        one_changed=False
        c+=1
        to_change =[]
        for point in screen:
            if screen[point]==".":
                around = [get_n(point,i+1) for i in range(4)]
                if any(screen.get(p)=="O" for p in around):
                    
                    to_change.append(point)
                    one_changed=True
        for point in to_change:
            screen[point]="O"
        ps(screen,pos)
        #time.sleep(1)
    print(c)

##    count ={}
##    count[(0,0)]=0
##    while True:
##        for point in screen:
##    
##            point=(-1,0)
##            if count.get(point):
##                continue
##            if screen.get(point) in (" ","#"):
##                continue
##            counts_around = [get_n(point,i+1) for i in range(4) ]
##   
##            counts_around = [count.get(p) for p in counts_around if p in count]
##   
##            if not counts_around:
##                continue
##            count[point] =1+min(counts_around)
##            if screen[point]=="O":
##                print(count[point])
##                raise Exception()
##    print(count)
        

if __name__ == "__main__":
    main()

