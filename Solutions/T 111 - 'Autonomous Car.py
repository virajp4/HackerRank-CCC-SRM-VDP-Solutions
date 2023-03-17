t = int(input())
while(t):
    a,b,c,d = map(int,input().split())
    tot = 0
    while(b<d):
        tot += b+a
        d -= b-a
    tot += d
    t-=1
    print(tot*c)