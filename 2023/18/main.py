input = "test.in"

with open(input, "r") as file:
    lines = file.readlines()

p = [0, 0]
pl = [[0, 0]]
dirs = {"R": [1, 0], "L": [-1, 0], "U": [0, 1], "D": [0, -1]}

for d, l, color in [x.split() for x in lines]:
    p[0] += dirs[d][0] * (int(l))
    p[1] += dirs[d][1] * (int(l))
    pl.append(p.copy())

area = 0

for i in range(len(pl) - 1):
    print(i)
#    area += (pl[i][0]) * (pl[i+1][1])
#    area -= (pl[i][1]) * (pl[i+1][0])
    area += (pl[i][0]) * (pl[i+1][1])
    area -= (pl[i][1]) * (pl[i+1][0])
print(pl)
print(area // 2)
