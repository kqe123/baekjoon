# 9063. 임씨의 이름이 새겨진 옥구슬의 위치 N 개가 주어질 때에, 임씨에게 돌아갈 대지의 넓이를 계산하는 프로그램을 작성하시오.
#  단, 옥구슬의 위치는 2 차원 정수 좌표로 주어지고 옥구슬은 같은 위치에 여러 개가 발견될 수도 있으며,
# x 축의 양의방향을 동쪽, y 축의 양의방향을 북쪽이라고 가정한다. 
import sys
N = int(input())
x_list = []
y_list = []
for i in range(N) :
    x, y = map(int, sys.stdin.readline().split())
    x_list.append(x)
    y_list.append(y)
extent = (max(x_list)-min(x_list))*(max(y_list)-min(y_list))
print(extent)
