def sum_of_digit(num):
    t_sum = 0
    for i in str(num):
        t_sum += int(i)
    return t_sum


for i in range(int(input())):
    n = int(input())
    while(sum_of_digit(n)%4 != 0):
        n += 1
    
    print(n)

    


        
