import numpy as np
def solution(x):
    a = str(x)
    a = [int(i) for i in a]
    print(a)
    b = np.array(a).sum()
    print(b)
    if x % b == 0 :
        answer = True
    else :
        answer = False
    return answer