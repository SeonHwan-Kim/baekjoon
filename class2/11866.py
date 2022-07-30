from collections import deque


from collections import deque
N, K = map(int, input().split())
q = [i for i in range(1, N + 1)]
dq = deque(q)
result = []
for i in range(N):
    dq.rotate(-(K - 1))
    result.append(dq.popleft())
print('<', ', '.join(map(str, result)), '>', sep='')
