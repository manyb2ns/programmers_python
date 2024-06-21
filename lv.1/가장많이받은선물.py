def calc_gift(gift_logs, f, x):
    if gift_logs[f][x] > gift_logs[x][f]:
        gift_logs[f]["next_gift"] += 1
    elif gift_logs[f][x] < gift_logs[x][f]:
        gift_logs[x]["next_gift"] += 1
    else:
        if gift_logs[f]["count"] > gift_logs[x]["count"]:
            gift_logs[f]["next_gift"] += 1
        elif gift_logs[f]["count"] < gift_logs[x]["count"]:
            gift_logs[x]["next_gift"] += 1
            
    return gift_logs

def set_logs(gift_logs, friends):
    for f in friends:
        gift_logs[f] = {}
        gift_logs[f]["count"] = 0 # 선물 준 횟수
        gift_logs[f]["next_gift"] = 0  # 다음 달 받는 선물 개수
        for name in friends:
            if name == f: continue
            gift_logs[f][name] = 0
            
    return gift_logs
            
def set_gift(gift_logs, gifts):
    for gift in gifts:
        g = gift.split() # 준 사람 [0] / 받은 사람 [1]
        gift_logs[g[0]][g[1]] += 1  # 준 사람
        gift_logs[g[0]]["count"] += 1   
        gift_logs[g[1]]["count"] -= 1   # 받은 사람
        
    return gift_logs

def solution(friends, gifts):
    answer = 0
    gift_logs = {} # 선물 준 횟수
    gift_logs = set_logs(gift_logs, friends)    # gift_logs 초기화
    gift_logs = set_gift(gift_logs, gifts)  # 선물 준 횟수 계산

    for f in friends:
        for x in friends:
            if f == x: continue
            calc_gift(gift_logs, f, x)
                
    for name in gift_logs:
        print(f"{name}: {gift_logs[name]}")
        if answer < gift_logs[name]["next_gift"]:
            answer = gift_logs[name]["next_gift"]
        
    return int(answer/2)
    
friends = ["a", "b", "c"]	
gifts = ["a b", "b a", "c a", "a c", "a c", "c a"]	

print(solution(friends, gifts))