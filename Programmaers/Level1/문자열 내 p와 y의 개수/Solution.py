def solution(s):
    pN = 0
    yN = 0
    for i in s :
        if i == 'p' or i == 'P' :
            pN+=1
        if i == 'y' or i == 'Y' :
            yN+=1
    
    if pN == yN :
        return True
    else :
        return False