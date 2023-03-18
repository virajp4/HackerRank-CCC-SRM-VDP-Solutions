def print_rangoli(size):
    # your code goes here
    a = "abcdefghijklmnopqrstuvwxyz"
    d = [a[i] for i in range(size)]
    items = list(range(size))
    items = items[:-1]+items[::-1]
    for i in items:
        temp = d[-(i+1):]
        row = temp[::-1]+temp[1:]
        print("-".join(row).center(size*4-3, "-"))