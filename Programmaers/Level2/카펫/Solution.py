import math

def get_divisor(num) :
    divisors = []
    length = int(math.sqrt(num)) + 1
    for i in range(1, length) :
        if num % i == 0 :
            divisors.append(i)
            divisors.append(num//i)
    divisors.sort()
    return divisors

def solution(brown, yellow):
    list_divisor = get_divisor(yellow)
    while list_divisor :
        maxval = list_divisor.pop()
        minval = list_divisor.pop(0)
        all_tyle = (maxval+2)*(minval+2)
        if all_tyle - yellow == brown :
            return [maxval+2, minval+2]