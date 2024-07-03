def solution(k, m, score):  # 사과 최대점수, 박스에 담기는 사과 개수, 사과 무더기
    answer = 0
    dict = {}   # 사과 점수(key)별 사과 개수(value)
    
    # 사과 최대점수(k)만큼 반복
    # 3부터 k까지 사과 점수별 사과 개수 카운트
    for i in range(1, k+1):
        if i in score:
            dict[i] = score.count(i)
    
    # 사과 점수가 높은 것부터 반복문 시작
    # (m보다 모자를 경우 그 아래 값으로 count 넘겨주기)
    i = 0
    key_array = list(reversed(dict.keys()))
    for key in key_array:
        if dict[key] % m == 0:  answer += key * dict[key]
        else:
            answer += key * (dict[key] - (dict[key]%m))
            # if key >= 2: dict[key_array[i+1]] += dict[key] % m
            if i < len(key_array)-1 : dict[key_array[i+1]] += dict[key] % m
        i += 1

    return answer

# print(solution(3, 4,[1, 2, 3, 1, 2, 3, 1])) # 8
# print(solution(4, 3,[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2])) # 33
# print(solution(5, 10, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) # 10
# print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2, 1])) # 33
# print(solution(4, 4, [4, 4, 3, 3, 3, 2, 2, 2, 1]))  # 20
# print(solution(9,2,[7, 7, 6, 5, 2])) # 24
print(solution(7,2,[7, 7, 5, 3, 3, 3, 1])) # 답 26

