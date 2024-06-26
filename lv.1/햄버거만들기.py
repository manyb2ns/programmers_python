def solution(ingredient):
    n, answer = 0, 0
    
    while True:
        if n+4 > len(ingredient):
            break
        if ingredient[n] != 1 or ingredient[n+1] != 2 or ingredient[n+2] != 3 or ingredient[n+3] != 1:
            n += 1
            continue
        else:
            for i in range(n+3, n-1, -1): ingredient.pop(i)            
            answer += 1
            if n >= 3: n = n-3
            else: n = 0
            
    return answer