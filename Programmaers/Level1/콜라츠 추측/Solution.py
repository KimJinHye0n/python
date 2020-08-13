def solution(num):
    n = 0
    while num != 1:
        if num % 2 == 0 :
            num = num / 2
            n = n + 1
        else :
            num = 3 * num + 1
            n = n + 1
        
        if n == 501 :
            n = -1
            break
    
    return n