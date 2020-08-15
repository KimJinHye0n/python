def solution(N, stages):
    ns = {}
    for i in range(1,N+1) :
        count = 0
        fail = 0
        for j in stages :
            if i <= j :
                count += 1
            if i == j :
                fail += 1
        try :
            ns[i] = fail/count
        except :
            ns[i] = 0
    ns = sorted(ns.items(), reverse = True, key = lambda item : item[1])
    answer = [i for i,j in ns]
    return answer