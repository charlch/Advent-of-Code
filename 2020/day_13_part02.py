print("Day 13 part 2")

data = """17,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,739,x,29,x,x,x,x,x,x,x,x,x,x,13,x,x,x,x,x,x,x,x,x,23,x,x,x,x,x,x,x,971,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,19"""

data = [(i,int(v)) for i,v in enumerate(data.split(",")) if v !="x"]
print(data)



still_to_lock_in = set(data)
step = 1
t=0
while still_to_lock_in:
    t=t+step
    to_remove = set()
    for eq  in still_to_lock_in:
       a,b= eq
       if (t+a)%b == 0:
           print("Chevron",eq[0],"encoded")
           step *= b
           to_remove.add(eq)
    still_to_lock_in = still_to_lock_in-to_remove

print(t)
