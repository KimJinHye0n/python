def solution(n):
    x = [False, False] + [True] * (n-1)
    primes = []
    for i in range(2,n+1) :
        if x[i] :
            primes.append(i)
            for j in range(2*i,n+1,i) :
                x[j] = False
    answer = len(primes)
    return answer