#2562
#9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
#예를 들어, 서로 다른 9개의 자연수
#3, 29, 38, 12, 57, 74, 40, 85, 61
#이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.

import sys
num = list()
for i in range(9) :
    num.append(int(sys.stdin.readline().rstrip()))

print(max(num))
print(num.index(max(num))+1)

#tip : sys.stdin.readline().rstrip()도 문자열로 입력을 받으므로 다른 자료형으로 받고 
#      싶다면 형변환을 해야함.
#리스트.index(X) : 리스트중 첫번째 X의 위치를 반환
