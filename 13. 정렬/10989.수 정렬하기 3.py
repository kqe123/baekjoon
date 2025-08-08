# 10989. N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

import sys
N = int(input())
scope = 10000
# 1. 원소들을 카운팅할 리스트 초기화
counts = [0] * (scope+1)

# 2. 0~scope까지 해당 원소의 개수를 카운팅
for i in range(N) :
    a = int(sys.stdin.readline().rstrip())
    counts[a] += 1

for i in range(len(counts)) : 
    for _ in range(counts[i]) :
        print(i)


