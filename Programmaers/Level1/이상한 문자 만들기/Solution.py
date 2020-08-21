def solution(s):
    answer = ''
    s = s.split(' ')
    for i in s :
        for j,k in enumerate(i) :
            if j % 2 == 0 :
                answer+=k.upper()
            else :
                answer+=k.lower()
        answer+=' '
    answer = answer[:-1]
    return answer