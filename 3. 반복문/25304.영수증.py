# 25304. 영수증에 적힌, 
# 구매한 각 물건의 가격과 개수
# 구매한 물건들의 총 금액
# 을 보고, 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 검사해보자.
import sys
total = int(input())
T = int(input())

result = 0
for i in range(T) :
    a, b = map(int, sys.stdin.readline().split())
    result += (a*b)

if result == total :
    print("Yes")
else : 
    print("No")
