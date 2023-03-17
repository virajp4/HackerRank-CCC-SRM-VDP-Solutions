n = int(input())
count = 0
for i in range(2, n+1):
    num = n
    while num % i == 0:
        num //= i
    if num%(i-1) == 0:
        count += 1
print(count)