from utils import *


#target area: x=56..76, y=-162..-134
t_min, t_max=Point(56,-162),Point(76,-134)
#target area: x=20..30, y=-10..-5
#t_min, t_max=Point(20,-10),Point(30,-5)

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

def y_gets_into_range(y_traj, y_min,y_max):
    y=0
    while y>=y_min:
        y+=y_traj
        
        y_traj-=1
        
        if y_min<=y<=y_max:
            return True
    return False            


def find_x_tragectories_which_hit(t_min, t_max):
    x_trajs = []
    for x_traj in range(1,t_max.x+1):

        if x_gets_into_range(x_traj,t_min.x, t_max.x):
            x_trajs.append(x_traj)
    return x_trajs

def find_y_tragectories_which_hit(t_min, t_max):
    y_trajs = []
    for y_traj in range(t_min.y,1000):

        if y_gets_into_range(y_traj,t_min.y, t_max.y):
            y_trajs.append(y_traj)
    return y_trajs        

xs = find_x_tragectories_which_hit(t_min, t_max)
print(xs)

ys = find_y_tragectories_which_hit(t_min, t_max)
print(ys)


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

c=0
for x in xs:
    for y in ys:
        if does_hit(Point(x,y),t_min, t_max):
           c+=1
print(c,my)
