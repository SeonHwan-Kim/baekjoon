n = int(input())
A = [input() for i in range(n)]
for i in A:
    count, sum = 0, 0
    for j in range(len(i)):
        if(i[j] == "O"):
            count += 1
            sum += count
        else:
            count = 0
    print(sum)