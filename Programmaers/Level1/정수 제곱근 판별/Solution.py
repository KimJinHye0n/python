import math
def solution(n):
    answer = 0
    if math.sqrt(n) - int(math.sqrt(n)) == 0 :
        x = math.sqrt(n) + 1
        answer = int(math.pow(x,2))
    else :
        answer = -1
    return answer