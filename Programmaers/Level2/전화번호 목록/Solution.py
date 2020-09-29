import heapq
def solution(phone_book):
    answer = True
    heapq.heapify(phone_book)
    while len(phone_book) :
        min_val = heapq.heappop(phone_book)
        for i in phone_book :
            for j in range(len(i)) :
                if min_val == i[j:len(min_val)] :
                    answer = False
                    break
            break
    return answer