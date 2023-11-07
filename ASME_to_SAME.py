for i in range(int(input())):
    N = int(input())
    s = input()
    t = input()
    hashmap = {}
    count = 0
    for i in t:
        if i in hashmap:
            hashmap[i] +=1
        else:
            hashmap[i] = 1
    for j in s:
        if j == "?":
            count += 1
        if j in hashmap and hashmap.get(j) > 0:
            hashmap[j] -= 1

    if count == sum(hashmap.values()):
        print("Yes")
    else:
        print("No")
