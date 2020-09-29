from itertools import combinations
import heapq

def solution(number, k):
    index_list = [i for i in range(len(number))]
    number_list = [i for i in number]
    combi = list(combinations(index_list, len(number)-k))
    lists = []
    for i in combi :
        numbers = ''.join([number_list[x] for x in i])
        lists.append(int(numbers))
    x = []
    for j in lists :
        heapq.heappush(x, (-j,j))
    answer = heapq.heappop(x)[1]
    return str(answer)