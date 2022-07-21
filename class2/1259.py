import sys
result = []
while True:
    s = sys.stdin.readline().rstrip()
    if s == '0':
        break
    else:
        start = 0
        end = len(s) - 1
        while start <= end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                result.append('no')
                break
        if start > end:
            result.append('yes')
print("\n".join(result))