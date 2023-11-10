for _ in range(int(input())):
    x = int(input())
    A = list(map(int,input().split()))
    d = {}

    for i in range(x):
        if A[i] in d.keys():
            d[A[i]][0] = i
        else:
            d[A[i]] = [i,i]

    total_sum = 0
    for keys in d:
        total_sum += (d[keys][0]-d[keys][1])
    print(total_sum)        
