def solution(a, b):
    day = ['THU', 'FRI', 'SAT','SUN', 'MON', 'TUE', 'WED']
    days = [31,29,31,30,31,30,31,31,30,31,30,31]
    x = 0
    for i in range(1,a) :
        x+=days[i-1]
    x = x+b
    y = x % 7
    answer = day[y]
    return answer