# 2720. 거스름돈의 액수가 주어지면 리암이 줘야할 쿼터(Quarter, $0.25)의 개수, 다임(Dime, $0.10)의 개수, 니켈(Nickel, $0.05)의 개수, 페니(Penny, $0.01)의 개수를 구하는 프로그램을 작성하시오. 거스름돈은 항상 $5.00 이하이고, 손님이 받는 동전의 개수를 최소로 하려고 한다.
# 예를 들어, $1.24를 거슬러 주어야 한다면, 손님은 4쿼터, 2다임, 0니켈, 4페니를 받게 된다.
import sys
T = int(input())
coins = [0,0,0,0]
for _ in range(T) :
    value = int(sys.stdin.readline().rstrip())
    coins[0] = value // 25
    value %= 25
    coins[1] = value // 10
    value %= 10
    coins[2] = value // 5
    value %= 5
    coins[3] = value
    for i in range(4) :
        print(coins[i],end=" ")
    print()