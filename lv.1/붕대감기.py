def solution(bandage, health, attacks):
    chealth = health # 현재 체력
    ctime, aidx = 0, 0 # 연속 성공 시간 / attacks 인덱스
    
    for time in range(attacks[-1][0]):
        print(time+1, "번째 차례")
        # 공격 검사
        if attacks[aidx][0]-1 == time:
            ctime = 0
            if chealth - attacks[aidx][1] > 0:
                chealth -= attacks[aidx][1]
                aidx += 1
                print(f"공격 시작 ---> 현재 체력: {chealth}")
                continue
            else:
                print(f"공격 시작 ---> DIE ")
                return -1
                
        # 붕대 감기
        if chealth + bandage[1] >= health:
            chealth = health
        else:
            chealth += bandage[1]

        ctime += 1            
        if ctime == bandage[0] and chealth + bandage[2] <= health:
            chealth += bandage[2]
            ctime = 0
        elif ctime == bandage[0]:
            chealth = health
            ctime = 0
            
        print(f"붕대 감기 ---> 현재 체력: {chealth}")
    
    return chealth


# print("\n남은 체력: ", solution([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]])) # 5
# print("\n남은 체력: ", solution([3, 2, 7], 20, [[1, 15], [5, 16], [8, 6]])) # -1
# print("\n남은 체력: ", solution([4, 2, 7], 20, [[1, 15], [5, 16], [8, 6]]))	# -1
# print("\n남은 체력: ", solution([1, 1, 1], 5, [[1, 2], [3, 2]])) # 3
# print("\n남은 체력: ", solution([1, 1, 1], 20, [[1, 5], [4, 1]])) # 18
# print("\n남은 체력: ", solution([2, 4, 4], 100, [[1, 96], [18, 1]])) # 99
# print("\n남은 체력: ", solution([2, 4, 4], 20, [[1, 10], [2, 9], [6, 16]])) # 1
# print("\n남은 체력: ", solution([5, 1, 100], 10, [[6, 5]])) # 5
# print("\n남은 체력: ", solution([10, 1, 10], 10, [[5, 5], [10, 9]])) # -1
# print("\n남은 체력: ", solution([10, 10, 100], 10, [[1, 15], [3, 1]])) # -1
# print("\n남은 체력: ", solution([3, 10, 1], 100, [[1, 5], [3, 5]])) # 95
# print("\n남은 체력: ", solution([3, 1, 10], 100, [[1, 5], [3, 5]])) # 95