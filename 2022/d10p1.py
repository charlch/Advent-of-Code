data = """noop
addx 3
addx -5"""
data="""addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

data = """noop
addx 33
addx -30
noop
noop
addx 7
addx 1
noop
noop
addx 3
addx 3
addx 3
addx -4
addx 5
addx 2
noop
addx 7
noop
addx 1
addx 4
noop
addx 1
addx -38
noop
addx 16
addx -13
addx 2
addx 7
noop
addx -2
addx -10
addx 17
addx -5
addx 10
noop
addx -15
addx 16
addx 2
noop
noop
addx 7
addx 3
addx -2
addx 2
addx 5
addx -38
addx 7
addx -6
addx 2
noop
addx 7
noop
addx 1
addx 4
noop
noop
noop
noop
noop
addx 3
noop
addx 3
addx 2
noop
addx 7
noop
addx -20
addx 21
addx 3
addx 1
addx -35
addx 1
addx 4
noop
addx 31
noop
addx -26
addx 5
noop
noop
addx -2
addx 25
addx -18
addx -13
addx 14
addx 2
noop
noop
noop
addx 6
addx 1
addx 5
addx 3
addx -2
addx -38
addx 24
addx -17
addx 5
noop
noop
addx -2
addx 31
addx -24
addx 7
addx -10
addx 6
noop
addx 3
addx 2
noop
noop
addx 7
addx -2
addx -26
addx 31
addx 5
addx -40
addx 5
addx 33
addx -31
noop
addx 1
addx 4
addx 1
addx 4
addx 20
noop
noop
addx -14
addx -1
addx 5
noop
noop
addx 1
addx 2
noop
noop
addx 7
noop
noop
noop
noop
noop
noop"""
X=1

history = [0]


for line in data.split("\n"):
    if line == "noop":
        history.append(X)
    else:
        command, V = line.split(" ")
        if command == "addx":
            history.append(X)
            history.append(X)
            X=X+int(V)

print(history)
interest = [20,60,100,140,180,220]
for i in interest:
    print(i, history[i], i*history[i] )

print(sum(i*history[i]  for i in interest))


for y in range(6):
    print("")
    for x in range(40):
        p = y*40+x +1

        if abs(history[p] - x)<2:
            print("#", end="")
        else:
            print(".", end="")