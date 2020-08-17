def solution(seoul):
    answer = ''
    for i,j in enumerate(seoul) :
        if j == "Kim" :
            answer = '김서방은 %d에 있다'%i
    return answer