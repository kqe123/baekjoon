# 1978. 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

N = int(input())
num_list = list(map(int, input().split()))
result = 0
for num in num_list :
    counts = 0
    if num == 1 : 
        continue
    for i in range(1,num+1) :
        if num % i == 0 :
            counts += 1
    
    if counts == 2 :
        result += 1
print(result)