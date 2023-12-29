import numpy as np

with open("test.in", "r") as file:
    al = []
    for line in file:
        al.append(np.array((list(line.rstrip()))))

a = np.vstack(al)

p = [0, 0]
d = [1, 0]
ret = 1
dm = []

def fn(p, d):
    if p[0] + d[0] >= a.shape[1] or p[1] + d[1] >= a.shape[0]:
        return False
    return a[p[0] + d[0]][p[1] + d[1]]

def search(p, d):
    if fn(p, d) == False:
        return
    if fn(p, d) == '.':
        p = [p[0] + d[0], p[1] + d[1]]
        search(p, d)
    if fn(p, d) == '/':
        return


search(p, d)



