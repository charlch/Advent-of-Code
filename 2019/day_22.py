print("Day 22")

data = """deal with increment 73
cut -8387
deal with increment 41
cut 190
deal with increment 4
cut 6396
deal with increment 47
cut -9579
deal with increment 47
cut -1296
deal with increment 2
cut 3807
deal with increment 75
cut 8267
deal with increment 53
cut 5108
deal with increment 20
cut -62
deal with increment 63
cut 4435
deal into new stack
deal with increment 2
cut 8436
deal with increment 52
cut 8420
deal with increment 70
cut -7602
deal with increment 39
cut 6737
deal into new stack
cut -3549
deal with increment 63
deal into new stack
cut -2925
deal with increment 59
cut -9525
deal with increment 12
deal into new stack
deal with increment 7
cut 4619
deal with increment 27
cut 7141
deal with increment 69
cut 5221
deal with increment 19
cut 4288
deal into new stack
deal with increment 64
cut -1618
deal with increment 63
cut -9384
deal with increment 24
deal into new stack
deal with increment 54
cut 429
deal into new stack
cut 2190
deal with increment 28
cut -4420
deal with increment 10
cut 6968
deal with increment 34
cut 8566
deal with increment 4
cut 8979
deal with increment 58
deal into new stack
deal with increment 17
deal into new stack
cut -3775
deal with increment 72
cut 3378
deal with increment 40
cut -7813
deal into new stack
deal with increment 26
deal into new stack
cut 5504
deal with increment 64
deal into new stack
cut 3592
deal with increment 13
cut 4123
deal into new stack
deal with increment 67
deal into new stack
cut 1943
deal with increment 72
cut -5205
deal into new stack
deal with increment 12
cut 1597
deal with increment 10
cut 4721
deal with increment 36
cut 3379
deal into new stack
cut -5708
deal with increment 61
cut 6852"""

def new_stack(deck):
    return deck[::-1]

def cut(deck, no):
    return deck[no:]+deck[0:no]

assert cut(list(range(10)),3)==[3,4,5,6,7,8,9,0,1,2]
assert cut(list(range(10)),-4)==[6,7,8,9,0,1,2,3,4,5]

def deal(deck, no):
    ndeck = [None]*len(deck)
    for i, d in enumerate(deck):
        ndeck[(i*no)%len(deck)] = d
    return ndeck

assert deal(list(range(10)), 3) == [0,7,4,1,8,5,2,9,6,3]

deck = range(10007)
for inst in data.split("\n"):
    if inst == "deal into new stack":
        deck=new_stack(deck)
    else:
        inst=inst.split(" ")
        if inst[0] == "deal":
            deck = deal(deck, int(inst[-1]))
        elif inst[0]=="cut":
            deck = cut(deck, int(inst[-1]))

print(deck.index(31))
            

    
