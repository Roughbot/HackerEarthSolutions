for _ in range(int(input())):
    B,G,K = map(int,input().split())
    Boys_count = B//K
    if B%K != 0:
        Boys_count += 1
    Girls_count = G//K
    if G%K != 0:
        Girls_count += 1
    
    print(Boys_count + Girls_count)
