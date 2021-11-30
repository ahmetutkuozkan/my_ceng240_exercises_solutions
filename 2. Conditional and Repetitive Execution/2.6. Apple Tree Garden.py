#G = [[30, 40, 20, 50], [60, 20, 40, 10], [50, 30, 70, 60], [30, 40, 40, 20]] #[50, 30, 70, 60]
G = [[20, 10, 20, 30, 80, 80, 50, 80, 40, 40], [20, 10, 50, 10, 20, 90, 90, 20, 60, 20],
     [50, 50, 90, 10, 60, 30, 60, 20, 40, 60], [20, 80, 60, 80, 90, 20, 20, 60, 80, 30],
     [10, 30, 50, 60, 20, 10, 90, 50, 80, 70]] #[20, 80, 60, 80, 90, 20, 20, 60, 80, 30]
M, N = len(G), len(G[0])
total_sum = 0
max_sum = 0
max_sum_row = 0
for i in range(0,M):
    total_sum = 0
    for j in range(0,N):
        total_sum+= G[i][j]

    if total_sum > max_sum :
        max_sum = total_sum
        max_sum_row = i
print(G[max_sum_row])