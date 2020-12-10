from parse import *
from utils import *
from collections import Counter
print("Day 10")

testdata = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

data="""8
131
91
35
47
116
105
121
56
62
94
72
13
82
156
102
12
59
31
138
46
120
7
127
126
111
2
123
22
69
18
157
75
149
88
81
23
98
132
1
63
142
37
133
61
112
122
128
155
145
139
66
42
134
24
60
9
28
17
29
101
148
96
68
25
19
6
67
113
55
40
135
97
79
48
159
14
43
86
36
41
85
87
119
30
108
80
152
158
151
32
78
150
95
3
52
49"""

testdata2="""16
10
15
5
1
11
7
19
6
12
4"""

data = [int(i) for i in data.split("\n")]
data.append(0)
data.append(max(data)+3)
data= sorted(data)

diffs = []

for i, j in zip(data[0:-1], data[1:]):
    diffs.append(j-i)
c = Counter(diffs)

print("Part 1: ",c[1]*c[3])



data = set(data)

def way_count(last_picked):
    if last_picked == max(data):
        return 1
    count = 0
    for i in range(1,4):
        if last_picked+i in data:
            count+= way_count(last_picked+i)
    return count

way_count = memoize(way_count)

print("Part 2: ",way_count(0))
