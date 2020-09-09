import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while scoville[0] < K :
        if len(scoville) == 1 :
            if scoville[0] == K :
                count+=1
            else :
                count = -1
            break
        else :
            min1 = heapq.heappop(scoville)
            min2 = heapq.heappop(scoville)
            x = min1 + min2*2
            heapq.heappush(scoville, x)
            count+=1
    return count