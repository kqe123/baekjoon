# 2738. N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.
import sys
N, M = map(int, input().split())
a = []
b = []
for _ in range(N) :
    value = list(map(int, sys.stdin.readline().split()))
    a.append(value)
for _ in range(N) :
    value = list(map(int, sys.stdin.readline().split()))
    b.append(value)

for i in range(N) :
    for j in range(M) :
        print(a[i][j] + b[i][j],end=" ")
    print()