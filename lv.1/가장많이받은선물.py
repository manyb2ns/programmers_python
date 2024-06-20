def solution(friends, gifts):
    answer = 0
    
    gift_logs = {}
    
    # gift_logs 초기화
    for f in friends:
        gift_logs[f] = {}
        gift_logs[f]["count"] = 0 # 선물 지수
        gift_logs[f]["next"] = 0  # 다음 달 받는 선물
        for name in friends:
            if name == f: continue
            gift_logs[f][name] = 0

    # 선물 지수 계산
    for gift in gifts:
        g = gift.split() # 받은 사람 [0] / 준 사람 [1]
        # 받은 사람
        gift_logs[g[0]][g[1]] += 1
        gift_logs[g[0]]["count"] += 1
        # 준 사람
        gift_logs[g[1]]["count"] -= 1

    for f in friends:
        for x in friends:
            if f == x: continue
            elif gift_logs[f][x] > gift_logs[x][f]:
                gift_logs[x]["next"] += 1
            elif gift_logs[f][x] < gift_logs[x][f]:
                gift_logs[f]["next"] += 1
            else:
                if gift_logs[f]["count"] > gift_logs[x]["count"]:
                    gift_logs[x]["next"] += 1
                elif gift_logs[f]["count"] < gift_logs[x]["count"]:
                    gift_logs[f]["next"] += 1
                else:
                    continue
                
    print(gift_logs)
    
friends = ["muzi", "ryan", "frodo", "neo"]
gifts = ["muzi frodo", "muzi frodo", "ryan muzi"]

solution(friends, gifts)