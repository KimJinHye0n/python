import collections

def solution(participant, completion):
    x = collections.Counter(participant)
    y = collections.Counter(completion)
    for key, value in x.items() :
        if y[key] != value :
            answer = key
    return answer