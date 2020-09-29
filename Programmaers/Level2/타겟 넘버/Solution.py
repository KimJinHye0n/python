def solution(numbers, target):
    answer_list = [0]
    for i in numbers :
        tmp = []
        for j in answer_list :
            tmp.append(j+i)
            tmp.append(j-i)
        answer_list = tmp
    return answer_list.count(target)