import re

with open("03.in", "r") as f:
    ls = f.readlines()

p = re.compile(r"mul\([0-9]*,[0-9]*\)")
p1 = re.compile(r"[0-9]+")
r = 0
for s in ls:
    matches = p.findall(s)
    for m in matches:
        nm = p1.findall(m)
        a = 1
        for y in nm:
            a *= int(y)
        r += a
    
print(r)

