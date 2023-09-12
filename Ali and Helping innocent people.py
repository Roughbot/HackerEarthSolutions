at = str(input())


def check(st):
    if st[2] in "AEIOUY" or len(st) != 9:
        return "invalid"
    else:  # DDXDDD-DD
        a = [int(st[0])+int(st[1]), int(st[3])+int(st[4]), int(st[4])+int(st[5]), int(st[7])+int(st[8])]
        if all(x%2==0 for x in a):
            return "valid"
        else:
            return "invalid"


print(check(at))