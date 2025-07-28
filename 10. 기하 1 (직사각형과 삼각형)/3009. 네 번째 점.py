# 3009. 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.
import sys
pos = {}
x, y = 0, 0
existY = 0
y_list = []
for i in range(3) : 
    a, b = map(int, sys.stdin.readline().split())
    if a not in pos :
        pos[a] = [b]
    else : 
        pos[a].append(b)

for key in pos :
    if len(pos[key]) == 2 :
        y_list = pos[key]
    else : 
        x = key
        existY = pos[key]

for target in y_list :
    if target not in existY :
        y = target

print(x, y)
