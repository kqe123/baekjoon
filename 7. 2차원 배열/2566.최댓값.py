# 2566. <그림 1>과 같이 9×9 격자판에 쓰여진 81개의 자연수 또는 0이 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 행 몇 열에 위치한 수인지 구하는 프로그램을 작성하시오.

import sys
grid = []
maximum = -1
pos = [-1,-1]
for i in range(9) :
    grid.append(list(map(int, sys.stdin.readline().split())))

for i in range(len(grid)) :
    for j in range(len(grid[i])) :
        if grid[i][j] >= maximum : 
            maximum = grid[i][j]
            pos = [i+1, j+1]

print(maximum)
print(pos[0],pos[1])