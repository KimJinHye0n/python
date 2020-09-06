def solution(s):
    whole = s.split()
    wholes = []
    for i in whole :
        wholes.append(float(i))
    minvalue = min(wholes)
    maxvalue = max(wholes)
    answer = str(int(minvalue)) + " " + str(int(maxvalue))
    return answer