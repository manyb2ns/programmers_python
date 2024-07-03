def solution(number, limit, power):
    answer = 0

    for n in range(1,number+1):
        divisor = 2
        values = {1, n}
        for i in range(1,int((n/2))+1):
            if i in values: continue
            elif n%i == 0:
                divisor += 1
                values.add(i)
                if int(n/i) not in values:
                    divisor += 1
                    values.add(int(n/i))
            if divisor >= limit: break

        if n == 1:              answer += 1
        elif divisor > limit:   answer += power
        else:                   answer += divisor

    return answer

print(solution(5,3,2))
print(solution(10,3,2))