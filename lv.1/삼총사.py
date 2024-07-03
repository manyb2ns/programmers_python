def solution(number):
    count = 0
    l = len(number)

    for idx1 in range(l-2):
        for idx2 in range(idx1+1, l-1):
            for idx3 in range(idx2+1, l):
                if number[idx1] + number[idx2] + number[idx3] == 0:
                    count += 1

    return count

# print(solution([-2, 3, 0, 2, -5]))
print(solution([0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]))