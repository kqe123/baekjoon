# 11651. 2차원 평면 위의 점 N개가 주어진다. 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
import sys
N = int(input())
dot = {}
for i in range(N) :
    x, y = map(int, sys.stdin.readline().split())
    if y in dot : 
        dot[y].append(x)
    else : 
        dot[y] = [x]

for key in sorted(dot) :
    for x in sorted(dot[key]) :
        print(x,key)