N = int(input())
value = 1
count = 1
while N > value:
    value += count * 6
    count += 1
print(count)