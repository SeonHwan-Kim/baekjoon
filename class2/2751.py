import sys
N = int(sys.stdin.readline().rstrip())
a = list([int(sys.stdin.readline().rstrip()) for i in range(N)])
a.sort()
print('\n'.join(map(str, a)))
