obj = input()

def chkword(name):
    z = 0
    o = 0
    for i in name:
        if i == 'z':
            z+=1
        elif i == 'o':
            o+=1
    print("Yes" if z*2 == o else "No")

if len(obj) <= 20:
    chkword(obj)
