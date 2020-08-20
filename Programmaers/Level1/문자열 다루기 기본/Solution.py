def solution(s):
    a = [str(i) for i in range(0,10)]
    b = [i for i in s if i in a]
    if len(s) != len(b) :
        return False
    else : 
        if len(b) == 4 or len(b) == 6 :
            return True
        else :
            return False