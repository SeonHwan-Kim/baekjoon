import sys
T = int(sys.stdin.readline())
for i in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    if N % H == 0:
        floor = H * 100
        num = N // H
    else:
        floor = (N % H) * 100
        num = N // H + 1
    print(floor + num)