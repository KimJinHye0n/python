def solution(a, b):
    x = [i for i in range(min(a,b), max(a,b)+1)]
    answer = sum(x)
    return answer