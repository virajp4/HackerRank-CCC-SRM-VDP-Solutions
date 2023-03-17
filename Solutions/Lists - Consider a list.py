if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        task = list(input().split())
        if task[0]=='insert':
            a.insert(int(task[1]),int(task[2]))
        if task[0]=='remove':
            a.remove(int(task[1]))
        if task[0]=='append':
            a.append(int(task[1]))
        if task[0]=='sort':
            a.sort()
        if task[0]=='pop':
            a.pop()
        if task[0]=='reverse':
            a.reverse()     
        if task[0]=='print':
            print(a)