import enum
a = input().upper()
s = set(a)
ls = list(s)
count = [0 for i in range(len(s))]
for i in range(len(a)):
    for pos, char in enumerate(s):
        if(char == a[i]):
            count[pos] += 1
b = 0
for i in range(len(s)):
    if(max(count) == count[i]):
        b += 1
if(b > 1):
    print("?")
else:
    print(ls[count.index(max(count))])