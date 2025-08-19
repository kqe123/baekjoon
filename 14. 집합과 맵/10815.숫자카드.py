# 10815. 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.

import sys
N = int(sys.stdin.readline().rstrip())
cards = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().rstrip())
question_list = list(map(int, sys.stdin.readline().split()))
result = []

for i in question_list :
    if i not in cards : 
        result.append('0')
    else : 
        result.append('1')

print(" ".join(result))

# 깨달은점 : 1. for문안에서 print()를 남발하는것보다, join()을 이용해 문자열을 합쳐서 출력하는게 더 빠르다
#            2. list안에서 in 연산자를 쓰면 앞에서부터 찾기 때문에 최악의 경우 O(n)이 걸리지만,
#               set, dictionary는 해시 테이블을 쓰기 때문에 O(1)밖에 걸리지 않는다!

