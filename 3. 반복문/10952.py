#10952
#두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
#입력은 여러 개의 테스트 케이스로 이루어져 있다. 입력의 마지막에는 0 두 개가 들어온다.
import sys
while True :
    a, b = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0 : break
    else : print(a+b)
