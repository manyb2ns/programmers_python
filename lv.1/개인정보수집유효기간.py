from datetime import datetime
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):
    result = []
    dt_today = datetime.strptime(today, "%Y.%m.%d")
    
    dict_terms = {}
    for term in terms:
        term, month = term.split()
        dict_terms[term] = month

    for i, privacy in enumerate(privacies):
        pdate, pterm = privacy.split()
        pdate = datetime.strptime(pdate, '%Y.%m.%d')
        vdate = (pdate + relativedelta(months=int(dict_terms[pterm])))

        if vdate <= dt_today:
            result.append(i+1)
    
    return result
    
# 검증
print(solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))   # [1, 3]