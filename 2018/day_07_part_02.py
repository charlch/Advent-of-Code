from collections import defaultdict
test_data= """Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin."""
data="""Step A must be finished before step I can begin.
Step M must be finished before step Q can begin.
Step B must be finished before step S can begin.
Step G must be finished before step N can begin.
Step Y must be finished before step R can begin.
Step E must be finished before step H can begin.
Step K must be finished before step L can begin.
Step H must be finished before step Z can begin.
Step C must be finished before step P can begin.
Step W must be finished before step U can begin.
Step V must be finished before step L can begin.
Step O must be finished before step N can begin.
Step U must be finished before step I can begin.
Step D must be finished before step P can begin.
Step Q must be finished before step L can begin.
Step F must be finished before step Z can begin.
Step L must be finished before step N can begin.
Step P must be finished before step S can begin.
Step I must be finished before step S can begin.
Step S must be finished before step R can begin.
Step T must be finished before step N can begin.
Step N must be finished before step X can begin.
Step Z must be finished before step J can begin.
Step R must be finished before step J can begin.
Step J must be finished before step X can begin.
Step E must be finished before step I can begin.
Step T must be finished before step R can begin.
Step I must be finished before step N can begin.
Step K must be finished before step C can begin.
Step B must be finished before step D can begin.
Step K must be finished before step T can begin.
Step E must be finished before step P can begin.
Step F must be finished before step I can begin.
Step O must be finished before step U can begin.
Step I must be finished before step J can begin.
Step S must be finished before step Z can begin.
Step L must be finished before step J can begin.
Step F must be finished before step T can begin.
Step F must be finished before step P can begin.
Step I must be finished before step T can begin.
Step G must be finished before step S can begin.
Step V must be finished before step U can begin.
Step F must be finished before step R can begin.
Step L must be finished before step R can begin.
Step Y must be finished before step D can begin.
Step M must be finished before step E can begin.
Step U must be finished before step L can begin.
Step C must be finished before step D can begin.
Step W must be finished before step N can begin.
Step S must be finished before step N can begin.
Step O must be finished before step S can begin.
Step B must be finished before step T can begin.
Step V must be finished before step T can begin.
Step S must be finished before step X can begin.
Step V must be finished before step P can begin.
Step F must be finished before step L can begin.
Step P must be finished before step R can begin.
Step D must be finished before step N can begin.
Step C must be finished before step L can begin.
Step O must be finished before step Q can begin.
Step N must be finished before step Z can begin.
Step Y must be finished before step L can begin.
Step B must be finished before step K can begin.
Step P must be finished before step Z can begin.
Step V must be finished before step Z can begin.
Step U must be finished before step J can begin.
Step Q must be finished before step S can begin.
Step H must be finished before step F can begin.
Step E must be finished before step O can begin.
Step D must be finished before step F can begin.
Step D must be finished before step X can begin.
Step L must be finished before step S can begin.
Step Z must be finished before step R can begin.
Step K must be finished before step X can begin.
Step M must be finished before step V can begin.
Step A must be finished before step M can begin.
Step B must be finished before step W can begin.
Step A must be finished before step P can begin.
Step W must be finished before step Q can begin.
Step R must be finished before step X can begin.
Step M must be finished before step H can begin.
Step F must be finished before step S can begin.
Step K must be finished before step Q can begin.
Step Y must be finished before step Q can begin.
Step W must be finished before step S can begin.
Step Q must be finished before step T can begin.
Step K must be finished before step H can begin.
Step K must be finished before step D can begin.
Step E must be finished before step T can begin.
Step Y must be finished before step E can begin.
Step A must be finished before step O can begin.
Step G must be finished before step E can begin.
Step C must be finished before step O can begin.
Step G must be finished before step H can begin.
Step Y must be finished before step I can begin.
Step V must be finished before step S can begin.
Step B must be finished before step R can begin.
Step B must be finished before step X can begin.
Step V must be finished before step I can begin.
Step N must be finished before step J can begin.
Step H must be finished before step I can begin."""

#data=test_data
nodes = defaultdict(set)
for line in data.split("\n"):
    
    a=line.split(" ")[1]
    b=line.split(" ")[7]

    nodes[b].add(a)
    nodes[a]


print(nodes)
done = ""
time=0
workers = [[i+1, ".", -1] for i in range(5)]
being_worked_on=set()
while True:

    just_finished =set()
    for worker in workers:
        if worker[2] == time:
            just_finished.add(worker[1])
            worker[1]="."
            worker[2]=-1

    for jf in just_finished:
        done+=jf
        being_worked_on.remove(jf)
        del nodes[jf]
        for a,b in nodes.items():
            if jf in b:
                b.remove(jf)

    for n in sorted(nodes.keys()):
        if len(nodes[n])==0 and n not in being_worked_on:
            #finder a worker for it
            for w in workers:
                if w[1]==".": #its a free one
                    w[1]=n
                    w[2]=time+60+(ord(n)-64)
                    being_worked_on.add(n)
                    break


    
    if len(done)==26:
        break
    time+=1
print(done, time)
            
    
