import sys
N = int(input())
q = []
for i in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        q.append(command[1])
    elif command[0] == 'pop':
        if len(q) > 0:
            print(q.pop(len(q) - 1))
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(q))
    elif command[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(q) == 0:
            print(-1)
        else:
            print(q[len(q) - 1])
