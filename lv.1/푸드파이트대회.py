def solution(food):
    answer = ''
    
    for f in range(1, len(food)):
        for i in range(int(food[f]/2)):
            answer = f"{answer}{f}"
    
    answer = f"{answer}0{answer[::-1]}"
    
    return answer

print(solution([1, 3, 4, 6])) # "1223330333221"