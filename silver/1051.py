n, m = map(int,input().split())
result = 0
value = [input() for j in range(n)]

if n == 1 or m == 1 : 
    result = 1
else : 
    maxlength = min(n,m)
    isfind = False
    for i in range(maxlength,1,-1) :
        x = 0 
        y = 0 
        while True : 
            if value[y][x] == value[y+i-1][x] == value[y][x+i-1] == value[y+i-1][x+i-1] :
                result = i * i 
                isfind = True
                break
            else :
                if (x+i-1) == (m-1) : 
                    if (y+i-1) == (n-1) :
                        break
                    else : 
                        x = 0 
                        y += 1
                else : 
                    x += 1
        if isfind == True : 
            break
if result == 0 : result = 1
print(result)

#N×M크기의 직사각형이 있다. 각 칸에는 한 자리 숫자가 적혀 있다. 
# 이 직사각형에서 꼭짓점에 쓰여 있는 수가 모두 같은 가장 큰 정사각형을 찾는 프로그램을 작성하시오. 
# 이때, 정사각형은 행 또는 열에 평행해야 한다.

#입력
#첫째 줄에 N과 M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 수가 주어진다.

#출력
#첫째 줄에 정답 정사각형의 크기를 출력한다.

           