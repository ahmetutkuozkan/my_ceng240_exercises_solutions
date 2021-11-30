T = [[1, 0, 0, 1, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [1, 1, 1, 0, 1], [0, 1, 0, 1, 1]]#True
#T = [[1, 0, 1, 1], [0, 1, 0, 1], [1, 0, 1, 0], [1, 1, 0, 1]]#True
#T = [[1, 0, 0], [1, 0, 1], [1, 0, 1]] #False
N = len(T)
Print = True
for i in range(N):
    if Print!=1 :
        break
    for j in range(N):
        if(T[i][j]!=T[j][i]):
            Print=0
            break
if Print==1:
    print("True")
else:
    print("False")