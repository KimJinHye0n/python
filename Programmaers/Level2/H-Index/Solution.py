def solution(citations):
    answer = 0
    for i in range(len(citations)) :
        x = [j for j in citations if j>=i]
        if len(x) == 0 : #case1
            answer = 0
        if i == len(x) : #case2
            answer = i
            break
        if i > len(x) : #case3
            answer = i-1
            break
        if len(x) == len(citations) :#case4
            answer = len(x)
    return answer