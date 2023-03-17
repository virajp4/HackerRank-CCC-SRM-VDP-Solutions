N = int(input())
if N == 1:
    print("Yes")
else:
    while N % 2 == 0 and N > 1:
        N /= 2
    if N == 1:
        print("Yes")
    else:  
        print("No")1