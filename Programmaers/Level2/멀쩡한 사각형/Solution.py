def solution(w,h):
    answer = w * h
    x = 0
    while w != h :
        x = w - h
        if (x < 0):
            answer -= w
            h = -x
        else :
            answer -= h
            w = x
    answer -= w
    return answer