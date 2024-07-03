def find_index(string):
    if string == "code": return 0
    elif string == "date": return 1
    elif string == "maximum": return 2
    elif string == "remain": return 3
    
def solution(data, ext, val_ext, sort_by):
    answer = []
    di = find_index(ext)
    si = find_index(sort_by)
    
    for i in range(len(data)):
        if data[i][di] < val_ext:
            answer.append(data[i])
    
    return sorted(answer, key=lambda x:x[si])

print(solution([[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]], "date", 20300501, "remain")) # [[3,20300401,10,8],[1,20300104,100,80]]

# test = [[10,"a"], [2, "b"], [3, "c"]]

# test_out = sorted(test, key=lambda x:x[0])
# print(test_out)