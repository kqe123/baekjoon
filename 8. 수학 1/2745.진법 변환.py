# 2745. B진법 수 N이 주어진다. 이 수를 10진법으로 바꿔 출력하는 프로그램을 작성하시오.
# 10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.
# A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35

N, radix = input().split()
radix = int(radix)
encoding = {chr(i):i-55 for i in range(55,91)}
digits = "0123456789"
result = 0 
power = 0
for i in range(len(N)-1,-1,-1) :
    if N[i] not in digits : 
        result += radix**power * encoding[N[i]]
    else : 
        result += radix**power * int(N[i])
    power += 1

print(result)