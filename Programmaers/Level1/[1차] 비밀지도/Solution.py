def solution(n, arr1, arr2):
    arr1map = []
    arr2map = []
    for i in arr1 :
        row = ''
        while i != 0 :
            if i % 2 == 0 :
                row += '0'
                i = i // 2
            else : 
                row += '1'
                i = i // 2
        row = row[::-1]
        row = row.zfill(n)
        x = []
        for j in row :
            x.append(j)
        arr1map.append(x)
    for i in arr2 :
        row = ''
        while i != 0 :
            if i % 2 == 0 :
                row += '0'
                i = i // 2
            else : 
                row += '1'
                i = i // 2
        row = row[::-1]
        row = row.zfill(n)
        x = []
        for j in row :
            x.append(j)
        arr2map.append(x)
    saves = ''
    for i in range(n) :
        for j in range(n) :
            alpha = int(arr1map[i][j]) + int(arr2map[i][j])
            if alpha > 0 :
                saves += '#'
            else :
                saves += ' '
    answer = ''
    answer = [saves[a : a+n] for a in range(0, len(saves), n)]
    return answer