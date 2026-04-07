
T = int(input())

for tc in range(T):

    L, U, X = map(int, input().split())
    
    if X < L:
        print(f"#{tc+1} {L-X}")
    elif L <= X and X <= U:
        print(f"#{tc+1} 0")
    else:
        print(f"#{tc+1} -1")
  