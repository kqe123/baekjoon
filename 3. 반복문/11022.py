#11022
#두 정수 A, B를 입력받은 다음 A+B를 출력하는 프로그램을 작성하시오.
#단, 각 테스트 케이스마다 "Case #x: A + B = C"형식으로 출력한다.
import sys
T = int(input())
for i in range(T) :
    a, b = map(int, sys.stdin.readline().split())
    print("Case #%d: %d + %d = %d" %(i+1,a,b,a+b))