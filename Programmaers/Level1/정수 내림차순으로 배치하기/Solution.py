def solution(n):
    answer = ''
    lists = []
    for i in str(n) :
        lists.append(i)
    lists = sorted(lists, reverse = True)
    for i in lists :
        answer += i
    return int(answer)