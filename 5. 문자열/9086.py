#9086
#문자열을 입력으로 주면 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 작성하시오.

import sys
T = int(input())
for i in range(T) :
    word = sys.stdin.readline().rstrip()
    print(word[0]+word[-1])


#TIP : 파이썬의 문자열은 음의 인덱스를 사용할수 있다. 인덱스 -1은 마지막 문자를 뜻함.
