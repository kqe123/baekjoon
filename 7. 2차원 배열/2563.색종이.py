# 2563. 가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지가 있다.
# 이 도화지 위에 가로, 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이를 색종이의 변과 도화지의 변이 평행하도록 붙인다.
# 이러한 방식으로 색종이를 한 장 또는 여러 장 붙인 후 색종이가 붙은 검은 영역의 넓이를 구하는 프로그램을 작성하시오.
import sys
T = int(input())
paper = [[1]*100 for i in range(100)]
counts = 0
for _ in range(T) :
    a, b = map(int, sys.stdin.readline().split()) 
    for i in range(b-1,b+9) :
        for j in range(a-1,a+9) :
            paper[i][j] = 0

for i in range(100) :
    counts += paper[i].count(0)
print(counts)

for j in range(len(a[0])) :
    for i in range(len(a)) :
        print(a[i][j])