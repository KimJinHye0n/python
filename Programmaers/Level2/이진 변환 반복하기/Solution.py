def bin_list(s):
    s = [i for i in bin(s)]
    s = s[2:]
    return s

def solution(s):
    s = [i for i in s]
    count_one = 0
    count_zero = 0
    count = 0
    while (len(s) > 1):
        count_one = s.count("1")
        count_zero += s.count("0")
        s = bin_list(count_one)
        count += 1
    answer = [count, count_zero]
    return answer