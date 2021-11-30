
#G = [[30, 40, 20, 50], [60, 20, 40, 10], [50, 30, 70, 60], [30, 40, 40, 20]] #[30, 60, 50, 30]

G = [[90, 10, 90, 40, 10],
     [70, 70, 80, 20, 30],
     [40, 60, 20, 90, 40],
     [40, 50, 50, 30, 20],
     [20, 30, 30, 80, 30],
     [90, 70, 20, 10, 60],
     [70, 90, 40, 40, 10]] #[90, 70, 40, 40, 20, 90, 70]


M, N = len(G), len(G[0])

array1 = [0]*M
total_sum = 0
max_sum = 0
max_sum_collum = 0
max_sum_row = 0
for i in range(0,N):
    total_sum = 0
    for j in range(0,M):
        total_sum+= G[j][i]


    if total_sum > max_sum:
        max_sum = total_sum
        max_sum_collum = j
        max_sum_row = i
        total_sum = 0


for i in range(0,M):
    array1[i] = G[i][max_sum_row]

print(array1)





