A, B = map(str, input().split())
rev_A = int(str(A)[::-1])
rev_B = int(str(B)[::-1])
if(rev_A > rev_B):
    print(rev_A)
else:
    print(rev_B)