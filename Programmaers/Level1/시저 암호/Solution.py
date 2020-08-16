def solution(phone_number):
    x = phone_number[-4:]
    y = len(str(phone_number)) - len(str(x))
    z = y*'*'
    answer = z + x
    return answer