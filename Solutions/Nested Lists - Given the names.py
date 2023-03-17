if __name__ == '__main__':
    res =[]
    sl = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        res+=[[name,score]]
        sl+=[score]
    
    b=sorted(list(set(sl)))[1] 

    for a,c in sorted(res):
        if c==b:
            print(a)