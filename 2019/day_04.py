c=0
for x in range(165432,707912):
    s = str(x)
    same = False
    allow=True
    
    for a,b in zip(s[0:-1],s[1:]):
      
        same = same or (a==b)
        if b<a:
            allow=False


    allow &=any([2*str(i)in s and not 3*str(i) in s for i in range(1,10)])
    if not same or not allow:
        continue
    c+=1

print(c)
