#2480
#1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.
#같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
#같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
#모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.
#3개 주사위의 나온 눈이 주어질 때, 상금을 계산하는 프로그램을 작성 하시오.

dice = list(map(int,input().split()))
if dice[0] != dice[1] and dice[1] != dice[2] and dice[0] != dice[2] :
    print(max(dice)*100)
elif dice[0] == dice[1] and dice[1] == dice[2] :
    print(10000+dice[0]*1000)
else : 
    if dice[0] == dice[1] or dice[1] == dice[2] :
        print(1000 + dice[1]*100)
    else : 
        print(1000 + dice[0]*100)