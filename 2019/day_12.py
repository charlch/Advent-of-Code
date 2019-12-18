import os  # NOQA
import sys  # NOQA
import re  # NOQA
import math  # NOQA
import fileinput
from string import ascii_uppercase, ascii_lowercase  # NOQA
from collections import Counter, defaultdict, deque, namedtuple  # NOQA
from itertools import count, product, permutations, combinations, combinations_with_replacement  # NOQA
from functools import reduce
from math import gcd

from utils import parse_line, parse_nums, mul, all_unique, factors, memoize, primes  # NOQA
from utils import new_table, transposed, rotated  # NOQA
from utils import md5, sha256, knot_hash  # NOQA
from utils import VOWELS, CONSONANTS  # NOQA
from utils import Point, DIRS, DIRS_4, DIRS_8  # NOQA

# Itertools Functions:
# product('ABCD', repeat=2)                   AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)                     AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)                     AB AC AD BC BD CD
# combinations_with_replacement('ABCD', 2)    AA AB AC AD BB BC BD CC CD DD

from computer import Process


def lcm(lst):
    return reduce(lambda x,y: x*y//gcd(x, y), lst)


class Moon():
    def __init__(self,x,y,z):
        self.pos=[x,y,z]
        self.vel=[0,0,0]

    def update_position(self):
        self.pos = [self.pos[i] +self.vel[i] for i in range(3)]

    def energy(self):
        return (sum(abs(a) for a in self.pos))*(sum(abs(a) for a in self.vel))

    def state(self,i):
        return (self.pos[i],self.vel[i])

states = set()
def main():
    print("Day 12")
    x = find_loop_size_each_axis(0)
    y = find_loop_size_each_axis(1)
    z = find_loop_size_each_axis(2)
    print(x,y,z)
    print(lcm([x,y,z]))
    
    


def find_loop_size_each_axis(t):
    moons =[Moon(-16,-1,-12),Moon(-11,11,0),
            Moon(0,-4,-17),
            Moon(2,2,-6)]

    for step in range(1000000000000):

        for moon_a in moons:
            #print(moon_a.pos, moon_a.vel)
            for moon_b in moons:
                for i in range(3):
                    if moon_b.pos[i]>moon_a.pos[i]:
                        moon_a.vel[i]+=1
                    elif moon_b.pos[i]<moon_a.pos[i]:
                        moon_a.vel[i]-=1
        for moon in moons:
            
            moon.update_position()
        state = tuple(moon.state(t) for moon in moons)
        if state in states:
            print(step)
            return step
        states.add(state)
        
        

if __name__ == "__main__":
    main()
