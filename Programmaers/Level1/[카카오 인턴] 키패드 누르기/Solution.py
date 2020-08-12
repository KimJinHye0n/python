def distance(x,y) :
    # 제곱으로 했을 때 안됐는데 절댓값으로 했을 때 풀림
    xd = abs(x[0] - y[0])
    yd = abs(x[1] - y[1])
    return xd+yd

def solution(numbers, hand):
    row_p = [0,1,2,3]
    column_p = [0,1,2]
    number = [1,2,3,4,5,6,7,8,9,'*',0,'#']
    list_p = [] # 좌표 표현
    for x in row_p :
        for y in column_p :
            list_p.append((x,y))
    
    answer = ''
    l_position = 9 # list_p의 좌표
    r_position = 11 # list_p의 좌표
    for i in numbers :
        if i == 1 or i == 4 or i == 7 or i == '*':
            answer+='L'
            l_position = number.index(i)
        if i == 3 or i == 6 or i == 9 or i == '#':
            answer+='R'
            r_position = number.index(i)
        if i == 2 or i == 5 or i == 8 or i == 0 :
            nump = number.index(i)
            ld = distance(list_p[nump],list_p[l_position])
            rd = distance(list_p[nump],list_p[r_position])
            if ld > rd :
                answer+='R'
                r_position = number.index(i)
            elif ld < rd :
                answer+='L'
                l_position = number.index(i)
            else :
                if hand == 'right' :
                    answer+='R'
                    r_position = number.index(i)
                else :
                    answer+='L'
                    l_position = number.index(i)
    return answer