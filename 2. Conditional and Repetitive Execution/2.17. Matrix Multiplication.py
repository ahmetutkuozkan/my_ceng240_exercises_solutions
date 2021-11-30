matrix1 = eval(input()); matrix2 = eval(input())
matrix1_l = len(matrix2)
matrix2_l = len(matrix2)
matrix2_l_row = len(matrix2[0])
new_matrix=[0]*matrix1_l
for i in range(matrix2_l):
    new_matrix[i]=[0]*matrix2_l_row
for row in range(matrix1_l):
    for column in range(matrix2_l_row):
        for i in range(matrix2_l):

            new_matrix[row][column]+= matrix1[row][i]*matrix2[i][column]



print(str(new_matrix))


