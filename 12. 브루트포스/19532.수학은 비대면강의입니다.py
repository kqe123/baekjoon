# 19532. 다음 연립방정식에서 x와 y의 값을 계산하시오.
# ax + by = c
# dx + ey = f
# 정수 a, b, c, d, e, f가 공백으로 구분되어 차례대로 주어진다.
# 문제에서 언급한 방정식을 만족하는 (x,y)가 유일하게 존재하고, 이 때 x와 y가 각각 -999이상 999 이하의 정수인 경우만 입력으로 주어짐이 보장된다.

a, b, c, d, e, f = map(int, input().split())
found = False
for x in range(-999,1000) :
    for y in range(-999,1000) :
        if a*x + b*y == c and d*x + e*y == f :
            print(x,y)
            found = True
            break
    if found == True :
        break

