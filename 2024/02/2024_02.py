with open("02.in", "r") as f:
    l = f.readlines()


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


print(r)
