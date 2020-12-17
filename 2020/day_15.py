from collections import defaultdict




def do_stuff(data):
    data = [int(d) for d in data.split(",")]

    turn=1
    last_spoken = {}
    last = -1
    while turn <=30000000:
        if turn %100000 ==0:
            print(turn)
        if turn<=len(data):
            num = data[turn-1]
        else:
            #print("Seeing if ",last, "is in ",last_spoken) 
            if last not in last_spoken:
                num = 0
            else:
                num = turn - last_spoken[last]-1
        #print("Turn",turn,"gives",num)
        #input()
        last_spoken[last] = turn-1
        last = num
        
        turn +=1

    return "Finished", num, data
    


#print(do_stuff("0,3,6"))
#print(do_stuff("1,3,2"))
#print(do_stuff("2,1,3"))
#print(do_stuff("1,2,3"))
#print(do_stuff("2,3,1"))
#print(do_stuff("3,2,1"))
#print(do_stuff("3,1,2"))
print(do_stuff("6,3,15,13,1,0"))
