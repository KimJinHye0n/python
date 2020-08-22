def solution(array, commands):
    answer = []
    for i in commands :
        x = sorted(array[i[0]-1 : i[1]])
        answer.append(x[i[2]-1])
    return answer