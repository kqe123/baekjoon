# 11022. 각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다. 
# x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B이다.
import sys
T = int(input())
for i in range(T) :
    a, b = map(int, sys.stdin.readline().split())
    print(f"Case #{i+1}: {a} + {b} = {a+b}")