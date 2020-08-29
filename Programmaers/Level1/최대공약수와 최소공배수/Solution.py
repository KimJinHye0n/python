def solution(n, m):
    a = max(n,m)
    b = min(n,m)
    c = 0
    while b!=0 :
        c = a % b
        a = b
        b = c
    answer = [a,m*n/a]
    return answer