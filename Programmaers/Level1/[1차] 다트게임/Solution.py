# 3번의 기회
# 0~10점
# S : 1제곱 / D : 2제곱 / T : 3제곱
# * : 해당점수 & 바로 전에 얻은 점수 2배 / 처음에 나오면 첫 점수만 2배(중첩가능)
# # : 해당 점수 마이너스
# *와 # 중첩시 : -2배
def SDT (lists) :
    x = []
    for l,i in enumerate(lists) :
        if i == 'S' :
            x.append(int(lists[l-1]))
        elif i == 'D' :
            x.append(int(lists[l-1]) ** 2)
        elif i == 'T' :
            x.append(int(lists[l-1]) ** 3)
        elif i == '#' :
            x[-1] = x[-1]*(-1)
        elif i == '*' :
            if len(x) == 1 :
                x[0] = x[0]*2
            elif len(x) > 1 :
                x[-1] = x[-1]*2
                x[-2] = x[-2]*2       
    return x
def solution(dartResult):
    lists = []
    numbers = [str(range(0,11))]
    for i in dartResult :
        lists.append(i)
    for i,j in enumerate(lists) :
        if lists[i] == '1' and lists[i+1] == '0' :
            del lists[i]
            lists[i] = '10'
    answer = sum(SDT(lists))
    return answer