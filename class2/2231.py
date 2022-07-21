import sys
N = int(sys.stdin.readline())
result = 0
for i in range(N):
    if sum(map(int, str(i))) + i == N:
        result = i
        break
print(result)