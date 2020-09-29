from collections import Counter
from functools import reduce

def solution(clothes):
    clothesdict = Counter()
    for i in clothes :
        clothesdict[i[1]] += 1
    answer = reduce(lambda x, y: x*(y+1), clothesdict.values(), 1) - 1
    return answer