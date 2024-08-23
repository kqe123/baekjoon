#25304
#영수증에 적힌,
#구매한 각 물건의 가격과 개수
#구매한 물건들의 총 금액을 보고, 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 검사해보자.

import sys
X = int(input())
N  = int(input())
sum = 0
for i in range(N) :
    price, num = map(int,sys.stdin.readline().split())
    sum += price*num

if sum == X : print("Yes")
else : print("No") 