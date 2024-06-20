def solution(t, p):
    answer = 0
    
    for i in range(len(t)-len(p)+1):
        t_ = t[i:i+len(p)]  # p 길이만큼 자른 t
        if t_ <= p: answer += 1
    
    return answer
    
print(solution("3141592", "271"))   # 2
print(solution("500220839878", "7"))    # 8
print(solution("10203", "15"))  # 3