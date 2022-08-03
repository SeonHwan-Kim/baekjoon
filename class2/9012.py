import sys
N = int(sys.stdin.readline().rstrip())
for i in range(N):
    bracket = sys.stdin.readline().rstrip()
    result = []
    for i in range(len(bracket)):
        if bracket[i] == '(':
            result.append(1)
        else:
            if(len(result) == 0):
                result.append(1)
                break
            result.pop()
    if len(result) == 0:
        print("YES")
    else:
        print("NO")
