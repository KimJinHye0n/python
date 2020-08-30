def solution(board, moves):
    moves = [i-1 for i in moves]
    result = []
    count = 0
    for i in moves :
        for j in range(len(board)) :
            if board[j][i] > 0 :
                if len(result) == 0 :
                    result.append(board[j][i])
                elif result[-1] == board[j][i] :
                    del result[-1]
                    count += 2
                else :
                    result.append(board[j][i])
                board[j][i] = 0
                break
    return count