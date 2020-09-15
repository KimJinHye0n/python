def solution(numbers):
    new_list = [(str(i)*3,i) for i in numbers]
    new_list = sorted(new_list, reverse = True)
    answer = ''
    for i,j in new_list :
        answer+=str(j)
    if answer[0] == '0' :
        answer = '0'
    return answer