def solution(priorities, location):
    priorities = [(i,j) for i, j in enumerate(priorities)]
    answer = 0
    while True :
        x = priorities.pop(0)
        # 첫 숫자와 나머지 모두 비교 (하나라도 있으면)
        if any(x[1] < i[1] for i in priorities) : 
            priorities.append(x)
        else :
            answer += 1
            if x[0] == location :
                return answer