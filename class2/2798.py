import sys
N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
result = []
for i in range(len(A)):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if A[i] + A[j] + A[k] < M:
                result.append(A[i] + A[j] + A[k])
print(max(result))