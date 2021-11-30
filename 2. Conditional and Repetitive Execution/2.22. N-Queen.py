board = [ ["_", "q", "q"]
    , ["_", "_", "_"]
    , ["q", "_", "_"]
          ]
a=0
N=len(board)
M=len(board[0])
for row in range(N):
    for column in range(M):
        if(board[row][column]=="q"):
            if row>0 and board[row-1][column]=="q": #N
                a=1
            if row<(M-1) and board[row+1][column]=="q": #S
                a=1
            if column<(N-1) and board[row][column+1]=="q":  #E
                a=1
            if column>0 and board[row][column-1]=="q": #W
                a=1
            if column<(N-1) and row>0 and board[row-1][column+1]=="q": #NE
                a=1
            if column>0 and row>0 and board[row-1][column-1]=="q": #NW
                a=1
            if column<(N-1) and row<(M-1) and board[row+1][column+1]=="q": #SE
                a=1
            if column>0 and row<(M-1) and board[row+1][column-1]=="q": #SW
                a=1
            if(board[row].count("q")>1):
                a=1


if(a==0):
    print("YES")
else:
    print("NO")
