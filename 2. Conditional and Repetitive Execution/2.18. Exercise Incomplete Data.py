R = [[0.464, 0.856, 'NaN', 0.126, 0.707],
     [0.822, 0.453, 0.941, 'NaN', 0.985],
     [0.535, 0.169, 'NaN', 0.334, 0.566],
     [0.136, 0.133, 0.513, 'NaN', 'NaN'],
     [0.054, 0.686, 0.19, 0.164, 0.737]]
R_column = int(len(R))
R_row = int(len(R[1]))
c=0
d=0
for column in range(R_column):
    for row in range(R_row):
        a=R[column][row]
        b=type(a) is str
        if(b==0):
            c+=R[column][row]
            d+=1
print(round(c/d,3))



