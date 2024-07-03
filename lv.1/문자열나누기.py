def solution(s):
    start, answer = 0, 0
    appear = [0, 0] # [0]: 첫 글자 등장 횟수 / [1]: 그 외 문자 등장 횟수

    for i in range(len(s)):
        if s[i] == s[start]:    appear[0] += 1
        else:   appear[1] += 1

        if (i+1) == len(s):
            answer += 1
        elif appear[0] == appear[1]:
            start = i + 1
            answer += 1
            appear = [0, 0]
    
    return answer

print(solution("banana"))   # 3
print(solution("abracadabra"))  # 6
print(solution("aaabbaccccabba"))   # 3