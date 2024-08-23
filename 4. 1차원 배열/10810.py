#10810
#도현이는 바구니를 총 N개 가지고 있고, 각각의 바구니에는 1번부터 N번까지 번호가 매겨져 있다. 또, 1번부터 N번까지 번호가 적혀있는 공을 매우 많이 가지고 있다. 
#가장 처음 바구니에는 공이 들어있지 않으며, 바구니에는 공을 1개만 넣을 수 있다.
#예를 들어, 2 5 6은 2번 바구니부터 5번 바구니까지에 6번 공을 넣는다는 뜻이다.
#공을 어떻게 넣을지가 주어졌을 때, M번 공을 넣은 이후에 각 바구니에 어떤 공이 들어 있는지 구하는 프로그램을 작성하시오.

import sys
N, M = map(int, input().split())
basket = list(0 for i in range(N)) #바구니 개수만큼 다 0으로 채운다.
for i in range(M) :
    a,b,num = map(int, sys.stdin.readline().split())
    for j in range(a-1,b) :  # 1번째~3번째까지 채운다면 실제론 0~2번째를 채워야되니
        basket[j] = num

for i in range(len(basket)) :
    print(basket[i],end=" ")