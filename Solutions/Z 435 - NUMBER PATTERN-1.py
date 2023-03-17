n = int(input())
for i in range(n+2):
    for j in range(1,i):
        print(j,end="")
    if i!=0 and i!=1:
        print()