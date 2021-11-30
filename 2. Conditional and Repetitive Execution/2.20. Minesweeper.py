B = [['m', 'm', '_', '_', '_'],
     ['m', 'm', '_', '_', '_'],
     ['_', '_', 'm', '_', '_']]
M = len(B); N = len(B[0])
answer = []
for row in range(M):
    new_row = []
    for column in range(N):
        if B[row][column]=='m':
            new_row.append('m')
        else:
            mine_number=0
            if row>0 and B[row-1][column]=='m': #N
                mine_number+=1
            if row<(M-1) and B[row+1][column]=='m': #S
                mine_number+=1
            if column<(N-1) and B[row][column+1]=='m':  #E
                mine_number+=1
            if column>0 and B[row][column-1]=='m': #W
                mine_number+=1
            new_row.append(mine_number)
    answer.append(new_row)


print(answer)

