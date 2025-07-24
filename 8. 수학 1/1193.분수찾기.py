# 1193. 이와 같이 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
# X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.

X = int(input())
target = 1 # 기준점
digit_sum = 2 # a와 b의 합
a = 0 # 분자
b = 0 # 분모
is_upwards = False # 분수를 찾아가는 방향 (오른쪽 위 대각선 방향, 왼쪽 아래 대각선 방향)

# 문제의 규칙에 따르면 1/1 -> 1/2 -> 2/1 이런식으로 이동을 하는데,
# X = 2~3이면 분자, 분모의 합이 3이고, X = 4~6이면 분자, 분모의 합이 4이다.
# 아래는 기준이 되는 X값의 최댓값(target)과 분자, 분모의 합(digit_sum)을 초기화하는 반복문이다.
while True :
    if target >= X :
        break
    target += digit_sum
    digit_sum += 1 
    if is_upwards == True :
        is_upwards = False
    else : 
        is_upwards = True

# digit_sum = 2이면 1/1이니 그대로 출력
if digit_sum == 2 : 
    print("1/1")

# is_upwards == True라면 target을 기준으로 오른쪽 위 대각선 방향으로 찾아야 되니 a는 점점 감소, b는 점점 증가
# is_upwards == False라면 반대로 a는 점점 증가, b는 점점 감소시키며 분수를 찾는다.
else : 
    if is_upwards : 
        a = digit_sum-1
        b = 1
        while target != X :
            a -= 1
            b += 1
            target -= 1
    else: 
        a = 1
        b = digit_sum-1
        while target != X :
            a += 1
            b -= 1
            target -= 1
    print(f"{a}/{b}")