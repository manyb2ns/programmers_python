def _reorder(ss_ascii):
    if (ss_ascii + 1) > 122:    # a = 97 / z = 122
        return (((ss_ascii + 1) % 122) + 97 - 1)
    else: return (ss_ascii + 1)

def solution(s, skip, index):    
    result = ""

    for ss in s:
        ss_ascii = ord(ss)
        count = 0   # 실제 이동 값 (skip 문자로 이동 값은 제외)

        while count != index:   # 실제 이동 값이 index와 같아질 때 loop 종료
            ss_ascii = _reorder(ss_ascii)   # ss_ascii +1 증가 && z 초과 시 a부터 순서 재조정

            if chr(ss_ascii) in skip:   continue    # skip에 포함 시 count 증가 없이 다음 loop
            else:   count += 1                      # skip에 미포함 시 count 증가

        result = f"{result}{chr(ss_ascii)}"

    return result

# 반례
print(solution("z","a",1)) # "b"
print(solution("a", "bcdefghijk", 20))  # "o"
print(solution("z","abcdefghij",20)) # "n"
print(solution("aukks","wbqd",5)) # "happy"
print(solution("abcde","bcd",2))  # "ffffg"
print(solution("yyyyy","za",2)) # "ccccc"
print(solution("ybcde","az",1)) # "bcdef"
print(solution("zzzzzz","abcdefghijklmnopqrstuvwxy",6)) # "zzzzzz"
print(solution("bcdefghijklmnopqrstuvwxyz", "a", 1))    # "cdefghijklmnopqrstuvwxyzb"