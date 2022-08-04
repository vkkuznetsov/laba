import numpy as np

M = int(input())
A = []
for i in range(M):
    A.append(list(map(int, input().split())))

arr_matrix = np.array(A)

for i in range(M//2):
    arr_time = np.array(arr_matrix[i])
    arr_matrix[i] = arr_matrix[M - 1 - i]
    arr_matrix[M - 1 - i] = arr_time

arr_trs = arr_matrix.transpose()

print(arr_trs)
