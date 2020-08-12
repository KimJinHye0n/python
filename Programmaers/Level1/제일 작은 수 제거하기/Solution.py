def solution(arr):
    minval = min(arr)
    arr.remove(minval)
    if len(arr) > 0 :
        answer = arr
    else :
        answer = [-1]
    return answer