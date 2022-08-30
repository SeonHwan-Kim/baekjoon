from collections import deque
import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    dq = deque(list(enumerate(map(int, sys.stdin.readline().split()))))
    max_value = max(map(max, dq))
    while True:
        if dq[0][1] == max_value:
            break
        else:
            dq.rotate(-1)
    count = 1
    for j in range(N):
        if dq.popleft()[0] == M:
            print(count)
            break
        else:
            count += 1
