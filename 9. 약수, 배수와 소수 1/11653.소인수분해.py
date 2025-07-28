# 11653. 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.
# 첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.
import math
N = int(input())
sieve = [True] * (N+1)
sieve[1] = False
result = []

# 1. sieve를 만든다. (N=1000라면 True가 1001개 들어있는 리스트를 만든다.)
# 2. N제곱근만큼 1~n제곱근까지 해당 수를 제외한 나머지 배수들을 전부 지운다. 
# 3. 그렇게 남은 소수들을 prime_list에 저장함.
for i in range(2, int(N**0.5)+1) :
    if sieve[i] == True :  
        for i in range(i*2, N+1, i) :
            sieve[i] = False
prime_list = [i for i in range(1,N+1) if sieve[i]]

# N을 소인수분해한다.
# 작은 소수부터 시작해서 N이 해당 소수로 나누어떨어지면 소인수분해시킨다.
while N not in prime_list :
    for prime in prime_list :
        if N % prime == 0 :
            result.append(prime)
            N //= prime
            break
result.append(N)

for r in result :
    print(r)


