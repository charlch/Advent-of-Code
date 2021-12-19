from utils import *
from time import time
_qt=time()
def qprint(a,b):
    global _qt
    if time()-_qt>1:
        _qt=time()
        print(a,b)

my=-10000000
def does_hit(traj, t_min, t_max):
    global my
    max_y = -100000000
    p=Point(0,0)
    while True:
        p=p+traj
        max_y = max(max_y,p.y)
        if traj.x>0:
            traj.x-=1
        if traj.x<0:
            traj.x+=1
        traj.y-=1



        if t_min.x<=p.x<=t_max.x:
            if t_min.y<=p.y<=t_max.y:
                my=max(my, max_y)
                
                return True

        if p.y<t_min.y:
            return False
        if p.x>t_max.x:
            return False

def x_gets_into_range(x_traj, x_min,x_max):
    x=0
    while x_traj!=0:
        x+=x_traj
        if x_traj>0:
            x_traj-=1
        elif x_traj<0:
            x_traj+=1

        if x_min<=x<=x_max:
            return True
    return False
            
        


print(does_hit(Point(9,0),Point(20,-10),Point(30,-5))        )

#target area: x=56..76, y=-162..-134
#target area: x=56..76, y=-162..-134
#Point(56,-163),Point(76,-134)

hits=set()

t_min, t_max=Point(56,-163),Point(76,-134)
t_min, t_max=Point(20,-10),Point(30,-5)
for x in range(1,t_max.x+1):
    if not x_gets_into_range(x,t_min.x, t_max.x):
        #print(x,"Cant get into range")
        continue
    
    for y in range(t_min.y,510):
        qprint(Point(x,y), len(hits))
        a = does_hit(Point(x,y),t_min, t_max)
        if a:
            hits.add(Point(x,y))
            #print("Hit", Point(x,y))

        
        
print(my, len(hits))
#print(hits)
#for h in hits:
#    print(does_hit(h,Point(56,-163),Point(76,-134)))
print(my, len(hits))
