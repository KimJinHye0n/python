def solution(s):
    answer = ''
    x = s[0]
    if ord(x) >= 97 and ord(x) <= 122 :
        answer += x.upper()
    else :
        answer += x
    y = [i.lower() for i in s[1:]]
    z = 1
    for i, j in enumerate(y) :
        if z :
            answer += j
        else :
            answer += j.upper()
            z = 1
        if j == ' ':
            z = 0
    return answer