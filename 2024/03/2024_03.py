import re

with open("03.in", "r") as f:
    ls = f.readlines()

# with open("03.test", "r") as f:
#     ls = f.readlines()

p = re.compile(r"(mul\([0-9]+,[0-9]+\))|(do\(\))|(don't\(\))")
p1 = re.compile(r"[0-9]+")
r = 0
do = True
for s in ls:
    matches = p.findall(s)
    for ms in matches:
        m = ""
        for mms in ms:
            if mms != "":
                m = mms
                break
        if m[:2] == "do":
            if m[2] == "n":
                do = False
            else:
                do = True
        else:
            if do and m != "":
                nm = p1.findall(m)
                a = 1
                for y in nm:
                    a *= int(y)
                r += a
    
print(r)

