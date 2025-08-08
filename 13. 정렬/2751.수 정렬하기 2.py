# 2751. N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
import sys
N = int(input())
num_list = []
for i in range(N) :
    num_list.append(int(sys.stdin.readline().rstrip()))

num_list.sort()
for i in range(N) :
    print(num_list[i])