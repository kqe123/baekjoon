# 11720. N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

N = int(input())
value = list(map(int,input()))
result = 0

for i in range(N) :
    result += value[i]
print(result)