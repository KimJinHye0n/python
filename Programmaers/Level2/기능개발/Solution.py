from collections import Counter

def solution(progresses, speeds):
    day_counts = []
    for h, i in enumerate(progresses) :
        p_s = speeds[h]
        standard = i
        days = 0
        while standard<100 :
            standard = standard + p_s
            days+=1
        if len(day_counts) == 0 :
            day_counts.append(days)
        elif day_counts[-1] <= days :
            day_counts.append(days)
        else :
            day_counts.append(day_counts[-1])
    print(day_counts)
    returns = Counter(day_counts)
    answer = [value for key, value in returns.items()]
    return answer