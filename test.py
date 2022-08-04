M = int(input())
A = [list(map(int, input().split())) for i in range(M)]
for i in range(M // 2):
    A[i], A[M - 1 - i] = A[M - 1 - i], A[i]
for i in range(M):
    print()
    for j in range(M):
        print(A[j][i], end=" ")
