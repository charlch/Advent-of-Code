from utils import *
from collections import defaultdict

data="""156, 193
81, 315
50, 197
84, 234
124, 162
339, 345
259, 146
240, 350
97, 310
202, 119
188, 331
199, 211
117, 348
350, 169
131, 355
71, 107
214, 232
312, 282
131, 108
224, 103
83, 122
352, 142
208, 203
319, 217
224, 207
327, 174
89, 332
254, 181
113, 117
120, 161
322, 43
115, 226
324, 222
151, 240
248, 184
207, 136
41, 169
63, 78
286, 43
84, 222
81, 167
128, 192
127, 346
213, 102
313, 319
207, 134
154, 253
50, 313
160, 330
332, 163"""

data2="""1, 1
1, 6
8, 3
3, 4
5, 5
8, 9"""

points = []
for l in data.split("\n"):
    points.append(Point(x=int(l.split(", ")[0]),y=int(l.split(", ")[1])))

print(points)

winners = 0

def do_point(a):
    global winners
    min_d = 100000000000000
    winning_point = None
    
    t = sum(a.dist_manhattan(p) for p in points)
    if t<10000:
        winners+=1
    

for y in range(-10,500):
    for x in range(-10,500):
        a = Point(x=x,y=y)
        do_point(a)


print(winners)

