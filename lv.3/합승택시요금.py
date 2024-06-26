import heapq

def list_to_dict(fares):
    dict_ = {}
    
    for f in fares:
        if f[0] not in dict_:
            dict_[f[0]] = {}
        if f[1] not in dict_:
            dict_[f[1]] = {}
        dict_[f[0]].update({ f[1]: f[2] })
        dict_[f[1]].update({ f[0]: f[2] })

    return dict_

def dijkstra(n, s, dict_):
    distance = {node: float('inf') for node in range(1, n+1)}
    distance[s] = 0
    queue = []
    
    heapq.heappush(queue, [distance[s], s])
    
    while queue:
        cur_dist, cur_node = heapq.heappop(queue)
        if(cur_dist > distance[cur_node]): continue
        
        for neighbor in dict_[cur_node]:
            if cur_dist + dict_[cur_node][neighbor] < distance[neighbor]:
                distance[neighbor] = cur_dist + dict_[cur_node][neighbor]
                heapq.heappush(queue, [distance[neighbor], neighbor])

    return distance

    
def solution(n, s, a, b, fares):

    dict_ = list_to_dict(fares)
    distances = {}
    answer = []
    
    for node in dict_:
        distances[node] = dijkstra(n, node, dict_)

    print(distances)

    # a, b 따로 갈 경우
    case_1 = distances[s][a] + distances[s][b]
    heapq.heappush(answer, case_1)
    
    # a->b 거쳐 갈 경우
    case_2 = distances[s][a] + distances[a][b]
    heapq.heappush(answer, case_2)
    
    # b->a 거쳐 갈 경우
    case_3 = distances[s][b] + distances[b][a]
    heapq.heappush(answer, case_3)
    
    case_4 = float('inf')
    # 합류 후 중간에서 따로 갈 경우 (Start 제외한 N-1만큼 조회)
    for n_ in range(1, n+1):
        if n_ == s: continue
        try:
            if distances[s][n_] + distances[n_][a] + distances[n_][b] < case_4:
                case_4 = distances[s][n_] + distances[n_][a] + distances[n_][b]
        except:
            continue
    heapq.heappush(answer, case_4)
    
    return heapq.heappop(answer)

# print(solution(
#     n=6,
#     s=4,
#     a=6,
#     b=2,
#     fares=	[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
# )) # 82

# print(solution(
#     n=6,
#     s=4,
#     a=5,
#     b=6,
#     fares=[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
# ))