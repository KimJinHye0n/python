def solution(s):
    answer = ''
    x = sorted(s, reverse = True)
    for i in x :
        answer += i
    return answer