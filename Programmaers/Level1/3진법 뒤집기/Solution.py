def change_base(n) :
    notation = '0123'
    q, r = divmod(n, 3)
    n = notation[r]
    return change_base(q) + n if q else n

def solution(n):
    n = change_base(n)
    answer = 0
    for i in range(len(n)) :
        answer += int(n[i])*3**i
    return answer