import queue
from collections import Counter

from parse import *

data="""Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

class Monkey:
    def __init__(self, items, operation, test, true_result, false_result):
        self.items = queue.Queue()
        for i in items:
            self.items.put(i)
        self.operation = operation
        self.test = test
        self.true_target = true_result
        self.false_target = false_result


'  Operation: new = old * 19'


monkeys= {0:Monkey([79, 98], lambda x:x* 19, 23, 2,3),
          1:Monkey([54, 65, 75, 74], lambda x:x+6,19,2,0),
          2:Monkey([79, 60, 97],lambda x:x*x,13,1,3),
          3:Monkey([74],lambda x:x+3,17,0,1),
          #4:Monkey([],,,,),2:Monkey([],,,,),
}


monkeys= {0:Monkey([85, 79, 63, 72], lambda x:x*17,2 ,2 ,6),
1:Monkey([53, 94, 65, 81, 93, 73, 57, 92], lambda x:x*x,7 ,0 ,2),
2:Monkey([62, 63], lambda x:x+7,13 ,7 ,6),
3:Monkey([57, 92, 56], lambda x:x+4, 5, 4,5),
4:Monkey([67], lambda x:x+5, 3, 1,5),
5:Monkey([85, 56, 66, 72, 57, 99], lambda x:x+6, 19,1 ,0),
6:Monkey([86, 65, 98, 97, 69], lambda x:x*13, 11,3 ,7),
7:Monkey([87, 68, 92, 66, 91, 50, 68], lambda x:x+2, 17,4 ,3),
}


inspections=Counter()

for round_number in range(20):
    for monkey_index in sorted(monkeys.keys()):
        monkey = monkeys[monkey_index]
        print(f"Monkey {monkey_index}")
        while not monkey.items.empty():
            item = monkey.items.get()
            print(f"  Monkey inspects an item with a worry level of {item}")
            inspections[monkey_index]+=1
            item = monkey.operation(item)
            print(f"    Worry level is now {item}")
            item = int(item/3)
            print(f"    Monkey gets bored with item. Worry level is divided by 3 to {item}.")
            if item % monkey.test == 0:
                print(f"    Current worry level IS divisible by {monkey.test}.")
                print(f"    Item with worry level {item} is thrown to monkey {monkey.true_target}.")
                monkeys[monkey.true_target].items.put(item)
            else:
                print(f"    Current worry level is not divisible by {monkey.test}.")
                print(f"    Item with worry level {item} is thrown to monkey {monkey.false_target}.")
                monkeys[monkey.false_target].items.put(item)
            pass


print(inspections)
a,b = sorted(inspections.values())[-2:]
print(a*b)