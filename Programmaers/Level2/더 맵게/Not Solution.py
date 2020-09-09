def scovileindex (a, b) :
    return a + b * 2

def solution(scoville, K):
    scoville = [i for i in scoville if i < K]
    count = 0
    while min(scoville) <= K :
        if len(scoville) == 1 :
            count+=1
            break
        else :
            minvalue1 = min(scoville)
            min1 = scoville.index(minvalue1)
            scoville.pop(min1)
            minvalue2 = min(scoville)
            min2 = scoville.index(minvalue2)
            scoville.pop(min2)
            scoville.append(scovileindex(minvalue1, minvalue2))
            count += 1
    return count