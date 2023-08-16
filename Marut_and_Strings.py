t = int(input())
if t in range(1,11):
    for i in range(0,t):
        obj = input()
        if len(obj) in range(1,101):
            if any(char.isalpha() for char in obj):
                upper_case = sum(1 for char in obj if char.isupper())
                lower_case = sum(1 for char in obj if char.islower())
                print( upper_case if upper_case < lower_case else lower_case)
            else:
                print('Invalid Input')
        else:
            print("Invalid Input")
elif t not in range(1,11):
    print("Invalid Test")
