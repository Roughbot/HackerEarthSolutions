def can_make_pieces(W, H, N):
    total_pieces = 1
    while W % 2 == 0 or H % 2 == 0:
        if W % 2 == 0:
            W //= 2
        else:
            H //= 2
        total_pieces *= 2
    
    return "Yes" if total_pieces >= N else "No"

for _ in range(int(input())):
    W, H, N = map(int, input().split())
    print(can_make_pieces(W, H, N))
