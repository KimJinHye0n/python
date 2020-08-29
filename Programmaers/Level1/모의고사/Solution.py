def problems(lists, answers) :
    a = len(answers) // len(lists)
    b = len(answers) % len(lists)
    x = lists*a + lists[:b]
    count = 0
    for i in range(len(answers)) :
        if x[i] == answers[i] :
            count+=1
    return count

def solution(answers):
    dicts = {}
    answer = []
    dicts[1] = problems([1,2,3,4,5],answers)
    dicts[2] = problems([2,1,2,3,2,4,2,5],answers)
    dicts[3] = problems([3,3,1,1,2,2,4,4,5,5],answers)
    maxdicts = max(dicts.values())
    for key, value in dicts.items() :
        if value == maxdicts :
            answer.append(key)
    return answer