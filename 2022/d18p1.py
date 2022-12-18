from utils import *

data = """"""

points = set()
for line in data split("\n"):
    parts = [int(a) for a in line.split(",")]
    points.add(Point3D(**parts))

c = 0

for p in points:
    c += len(a for a in DIRS3D if a +p not in points)

print(c)
