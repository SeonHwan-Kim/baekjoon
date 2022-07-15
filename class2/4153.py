import sys
result = []
while(True):
    a = list(map(int, sys.stdin.readline().split()))
    if(a == [0, 0, 0]):
        break
    else:
        max = max(a)
        a.remove(max)
        a = [i ** 2 for i in a]
        if(max ** 2 == a[0] + a[1]):
            result.append("right")
        else:
            result.append("wrong")
        del max
for i in range(len(result)):
    print(result[i])