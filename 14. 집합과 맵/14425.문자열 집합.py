# 14425. 총 N개의 문자열로 이루어진 집합 S가 주어진다.
# 입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 것이 총 몇 개인지 구하는 프로그램을 작성하시오.
import sys
N, M = map(int, input().split())
S = set()
check_list = set()

for i in range(N) :
    S.add(sys.stdin.readline().rstrip())
for i in range(M) :
    check_list.add(sys.stdin.readline().rstrip())

