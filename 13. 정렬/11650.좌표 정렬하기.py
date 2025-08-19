# 11650. 2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로,
# x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
import sys
T = int(input())
pos = {}
for i in range(T) :
    a, b = map(int, sys.stdin.readline().split())
    if a in pos :
        pos[a].append(b)
    else : 
        pos[a] = [b]

for key in pos :
    pos[key].sort()

# 딕셔너리를 sorted()하면 key를 기준으로 오름차순으로 정렬
for key in sorted(pos) : 
    for x in pos[key] :
        print(key, x)