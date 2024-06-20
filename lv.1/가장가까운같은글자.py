def solution(s):
    s_dict = {}
    answer = []
    i = 0
    
    for chr in s:
        if chr not in s_dict:
            s_dict[chr] = []
        s_dict[chr].append(i)

        if len(s_dict[chr]) == 1:
            answer.append(-1)
        elif len(s_dict[chr]) > 1:
            answer.append(s_dict[chr][-1] - s_dict[chr][-2])

        i += 1
    
    return answer

# solution("banana")
print(solution("banana")) # [-1, -1, -1, 2, 2, 2]
print(solution("foobar")) # [-1, -1, 1, -1, -1, -1]