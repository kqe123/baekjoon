#2675
#문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.
#QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

import sys
T = int(input())
for i in range(T) :
    counts, word = sys.stdin.readline().rstrip().split()
    counts = int(counts)
    for i in range(len(word)) :
        print(word[i]*counts,end="")
    print()

#문자열 연산 
# + : 문자열 연결
# * : 문자열 반복
