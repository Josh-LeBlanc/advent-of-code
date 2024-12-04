with open("02.in", "r") as f:
    l = f.readlines()

r = 0
# p1

for line in l:
    s = [int(x) for x in line.split(" ")]
    safe = True
    tol = True
    for i in range(len(s) - 1):
        if abs(s[i] - s[i+1]) > 3 or s[i] == s[i+1]:
            safe = False
            break
    ss = sorted(s)
    rs = sorted(s, reverse=True)
    if not ((s == ss) or (s == rs)):
        safe = False
    if safe:
        r += 1

print(r)

r = 0
for line in l:
    s = [int(x) for x in line.split(" ")]
    safe = True
    for i in range(len(s) - 1):
        if abs(s[i] - s[i+1]) > 3 or s[i] == s[i+1]:
            safe = False
            break
    ss = sorted(s)
    rs = sorted(s, reverse=True)
    if not ((s == ss) or (s == rs)):
        safe = False
    if safe:
        r += 1
    else:
        for i in range(len(s)):
            ts = s.copy()
            ts.pop(i)
            tsafe = True
            for j in range(len(ts) - 1):
                if abs(ts[j] - ts[j+1]) > 3 or ts[j] == ts[j+1]:
                    tsafe = False
                    break
            tss = sorted(ts)
            trs = sorted(ts, reverse=True)
            if not ((ts == tss) or (ts == trs)):
                tsafe = False
            if tsafe:
                r += 1
                break
print(r)
                    


