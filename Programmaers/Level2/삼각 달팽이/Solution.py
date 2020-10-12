import itertools

def solution(n):
    zero_list = []
    for i in range(n) :
        tmp = []
        for j in range(n) :
            tmp.append(0)
        zero_list.append(tmp)
    x, y = -1,0
    count = 1
    for i in range(n) : 
        for _ in range(n-i) :
            if i % 3 == 0 :
                x += 1
            elif i % 3 == 1 :
                y += 1
            else :
                x -= 1
                y -= 1
            zero_list[x][y] = count
            count += 1
    # zero_list = sum(zero_list, [])
    zero_list = list(itertools.chain.from_iterable(zero_list)) # 조금 더 빠르다
    answer = [i for i in zero_list if i > 0]
    return answer