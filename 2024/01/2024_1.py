from collections import Counter

l1 = []
l2 = []

with open("1.in", "r") as f:
    l = f.readline()
    while (l):
        s = l.split()
        l1.append(int(s[0]))
        l2.append(int(s[1]))
        l = f.readline()

l1.sort(), l2.sort()
sum = 0

for i in range(len(l1)):
    sum += abs(l1[i] - l2[i])

# part 1
print(sum)

rc = Counter(l2)

sum2 = 0
for x in l1:
    sum2 += x * rc[x]

print(sum2)
