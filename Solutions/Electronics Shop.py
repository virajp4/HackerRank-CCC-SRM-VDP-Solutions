import sys

s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
a = [int(kt) for kt in input().strip().split(' ')]
b = [int(pt) for pt in input().strip().split(' ')]
ans = -1
for x in a:
    for y in b:
        if x + y <= s:
            ans = max(ans, x + y)
            
print (ans)