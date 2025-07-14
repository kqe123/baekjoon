# 2525. 훈제오리구이를 시작하는 시각과 오븐구이를 하는 데 필요한 시간이 분단위로 주어졌을 때,
# 오븐구이가 끝나는 시각을 계산하는 프로그램을 작성하시오.

h, m = map(int, input().split())
take = int(input())

m += take
h += m//60
m = m%60
if h >= 24 :
    h = h % 24
print(h, m)