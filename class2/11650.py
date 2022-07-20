N = int(input())
A = [list(map(int, input().split())) for i in range(N)]
A.sort(key = lambda x : (x[0], x[1]))
for i in range(N):
    print(A[i][0], A[i][1])