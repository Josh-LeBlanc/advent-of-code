import numpy as np
import pandas

with open("11.in", "r") as file:

    arraylist = []

    for line in file:
        arraylist.append(np.array((list(line.rstrip()))))
        
full = np.vstack(arraylist)
skip_next = False

# double blank rows
i = 0
end = np.shape(full)[0]
while i < end:
    if "#" not in full[i, :]:
        row = np.array(np.full_like(full[i, :], "."))
        full = np.insert(full, i, row, axis=0)
        end += 1
        i += 1
    i += 1

end = np.shape(full)[1]
i = 0
while i < end:
    if "#" not in full[:, i]:
        col = np.array(np.full_like(full[:, i], "."))
        full = np.insert(full, i, col, axis=1)
        end += 1
        i += 1
    i += 1


starlist = []

# need to write space doubler first
for i in range(np.shape(full)[0]):
    for j in range(np.shape(full)[1]):
        if full[i][j] == "#":
            starlist.append((i, j))

restlist = starlist[1:]
ret = 0
pairs = 0

for i in range(len(starlist) - 1):
    for tup in restlist:
        ret += abs(starlist[i][0] - tup[0]) + abs(starlist[i][1] - tup[1])
        pairs += 1
    restlist.pop(0)

print(ret)


