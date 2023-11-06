def remove_k_digits(num, k):
    stack = []
    removed = 0
    
    for digit in str(num):
        # Remove smaller digits from the stack to maximize the number
        while removed < k and stack and stack[-1] < digit:
            stack.pop()
            removed += 1
        stack.append(digit)
    
    # If there are still digits to be removed, remove them from the end
    while removed < k:
        stack.pop()
        removed += 1
    
    # Convert the stack to a string and return the result
    result = ''.join(stack)
    return result

N,K = map(int,inpot().split())
print(remove_k_digits(N,K)
