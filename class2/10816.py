import sys
N = int(sys.stdin.readline().rstrip())
get = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().rstrip())
card = list(map(int, sys.stdin.readline().split()))
first, last = 0, N
for i in card:
    