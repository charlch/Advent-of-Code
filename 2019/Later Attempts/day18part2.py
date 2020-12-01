from utils import *
from collections import defaultdict, deque

data = """#######
#a.#Cd#
##@#@##
#######
##@#@##
#cB#.b#
#######"""

data="""###############
#d.ABC.#.....a#
######@#@######
###############
######@#@######
#b.....#.....c#
###############"""

mapp = {}
robs = []
width = 0
height = 0
all_keys=set()
door_positions = defaultdict(set)
for x,lin in enumerate(data.split("\n")):
    height=x
    for y, char in enumerate(lin):
        width=y
        mapp[Point(x=x, y=y)] = char
        if char == "@":
            robs.append(Point(x=x, y=y))
        if char in LETTERS:
            all_keys.add(char)
        if char in UPPER_LETTERS:
            door_positions[char].add(Point(x=x, y=y))
    

#state is
# * a map updated with the keys and door removed
# * position of 4 robots
# * list of found keys
# * total steps.

class State(object):
    def __init__(self, mapp, robots, got_keys, steps):
        self.mapp = mapp
        self.robots = robots
        self.got_keys = got_keys
        self.steps = steps

    def is_valid(self):
        for robot in self.robots:
            if self.mapp[robot] == "#":
                return False
            if self.mapp[robot] in UPPER_LETTERS:
                return False
        return True

    def update_for_robots(self):
        for robot in self.robots:
            if self.mapp[robot] in LETTERS:
                door = self.mapp[robot]
                self.got_keys.add(door)
                self.mapp[robot] = "."
  
                for d in door_positions[door.upper()]:
                    self.mapp[d] = "."

    def same_but_better(self, other):

        return  ((self.mapp == other.mapp) and
                 (self.robots == other.robots) and
                 (self.got_keys == other.got_keys) and
                 (self.steps<=other.steps))

    def get_point(self,x,y):
        p = Point(x=x,y=y)
        if p in self.robots:
            return "$"
        return self.mapp[p]
    
    def print(self):
        print("Keys: ",self.got_keys, "Steps: ",self.steps)
        for x in range(height+1):
            print("".join(self.get_point(x,y) for y in range(width+1)))
        #print(self.as_string())
        
            
    def is_finished(self):
        return self.got_keys == all_keys

    def copy(self):
        mapp = {}
        for a,b in self.mapp.items():
            mapp[a.copy()]=b
        robs=[]
        for rob in self.robots:
            robs.append(rob.copy())

        return State(mapp, robs,self.got_keys.copy(), self.steps)

    def as_string(self):
        o = str(sorted(self.got_keys)) + str(sorted(self.robots))
        for x in range(height+1):
            o += ("".join(self.get_point(x,y) for y in range(width+1)))
        return o
        
        


finished_states = set()
seen_states={}
to_work_on = deque()
start_state = State(mapp, robs, set(),0)
to_work_on.append(start_state)
while to_work_on:
    state = to_work_on.pop()
    
 
    
    if state.is_finished():
        finished_states.add(state)
        continue


    seen_states[state.as_string()]=state

    #state.print()
   
    #print("########################")
    for i,robot in enumerate(state.robots):
        for direction in DIRS_4:

            new_state = state.copy()
            new_state.steps += 1
            new_state.robots[i] = robot + direction

            if new_state.is_valid():
                new_state.update_for_robots()
                seen_state = seen_states.get(new_state.as_string())
                if seen_state:
                    
                    if seen_state.same_but_better(new_state):
                     
                        break
                
                
                
                to_work_on.append(new_state)
                #new_state.print()
    #print("########################")
    #input()

            





m =  min(s.steps for s in finished_states)

for s in finished_states:
    if s.steps == m:
        s.print()
