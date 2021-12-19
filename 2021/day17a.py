from utils import *
from time import time
_qt=time()
def qprint(s):
    global _qt
    if time()-_qt>1:
        _qt=time()
        print(s)


def does_hit(traj, t_min, t_max):
    max_y=-10000000
    p=Point(0,0)
    while True:
        p=p+traj
        max_y=max(max_y,p.y)
        if traj.x>0:
            traj.x-=1
        if traj.x<0:
            traj.x+=1
        traj.y-=1



        if t_min.x<=p.x<=t_max.x:
            if t_min.y<=p.y<=t_max.y:
                return max_y

        if p.y<t_min.y:
            return False
        if p.x>t_max.x:
            return False



print(does_hit(Point(6,9),Point(20,-10),Point(30,-5))        )


#target area: x=56..76, y=-162..-134
#Point(56,-163),Point(76,-134)
my=-10000000
for x in range(0,77):
    hit_yet = False
    for y in range(0,10000):
        qprint(Point(x,y))
        a = does_hit(Point(x,y),Point(56,-162),Point(76,-134))

        if a>my:
            my=a
            print(Point(x,y),a)
        
        
print(my)
