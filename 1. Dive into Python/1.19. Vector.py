x_1 = int(input()); y_1 = int(input()); x_2 = int(input()); y_2 = int(input()); x_3 = int(input()); y_3 = int(input())
p1 = (x_1, y_1); p2 = (x_2, y_2); p3 = (x_3, y_3)
i=0 ; j=1
vector = (p1[i]+p2[i], p1[j]+p2[j])
subtracted = (vector[i]-p3[i], vector[j]-p3[j])
print(vector); print(subtracted)