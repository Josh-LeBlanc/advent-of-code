
with open("1.in", "r") as file:
    c = file.read().strip()

s = c.split(",")
r = 0
for i in s:
    sum = 0
    for char in i:
        sum += ord(char)
        sum = sum * 17
        sum = sum % 256
    r += sum

print(r)
