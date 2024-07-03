def solution(k, score):
    s_list = [score[0]]
    answer = [score[0]]

    for s in score[1:]:
        if len(s_list) < k:
            s_list.append(s)
            answer.append(min(s_list))
        else:
            s_min = min(s_list)
            if s_min < s:
                s_list[s_list.index(s_min)] = s
            answer.append(min(s_list))

    return answer

# solution(3, [10, 100, 20, 150, 1, 100, 200]) ---> [10, 10, 10, 20, 20, 100, 100]
print(solution(3, [10, 100, 20, 150, 1, 100, 200]))
print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))