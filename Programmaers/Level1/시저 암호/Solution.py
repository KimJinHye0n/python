# 아스키코드 : A - 65 / Z - 90 / a - 97 / z - 122 / 공백 - 32
# chr : 아스키코드 -> 문자 / ord : 문자 -> 아스키코드
def solution(s, n):
    answer = ''
    for i in s :
        if ord(i) == 32 :
            answer+=i
        else :
            if ord(i) >= 65 and ord(i) <= 90 :
                ordn = ord(i) + n
                if ordn > 90 :
                    ordn = ordn - 91 + 65
                answer+=chr(ordn)
            elif ord(i) >= 96 and ord(i) <=122 :
                ordn = ord(i) + n
                if ordn > 122 :
                    ordn = ordn - 123 + 97
                answer+=chr(ordn)
    return answer