# 2884. 상근이는 모든 방법을 동원해보았지만, 조금만 더 자려는 마음은 그 어떤 것도 없앨 수가 없었다.
# 이런 상근이를 불쌍하게 보던 창영이는 자신이 사용하는 방법을 추천해 주었다.
# 바로 "45분 일찍 알람 설정하기"이다.
# 현재 상근이가 설정한 알람 시각이 주어졌을 때, 창영이의 방법을 사용한다면, 이를 언제로 고쳐야 하는지 구하는 프로그램을 작성하시오.

hour, minute = map(int, input().split())
if minute >= 45 : 
    minute -= 45
else : 
    minute = 60 - (45-minute)
    if hour == 0 : 
        hour = 23
    else : 
        hour -= 1
print(hour, minute)