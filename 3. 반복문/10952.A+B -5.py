# 10952. 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 각 테스트 케이스마다 A+B를 출력한다.
import sys
while True : 
    a, b = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0 : 
        break
    print(a+b)

