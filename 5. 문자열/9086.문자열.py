# 9086. 문자열을 입력으로 주면 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 작성하시오.
import sys
T = int(input())
for _ in range(T) :
    word = sys.stdin.readline().rstrip()
    print(word[0]+word[-1])
