# 2750. N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
import sys
N = int(input())
num_list = []
for i in range(N) :
    num_list.append(int(sys.stdin.readline()))

# 버블 정렬 : 두 인접한 원소끼리 비교하여 두 원소를 교환하면서 정렬함.
# 원소가 N개라면 N-1회전까지 존재하고, 1회전에는 처음부터 끝까지 원소 2개씩 비교한다.
# 1회전이 끝난 후는 맨 뒤의 원소는 정렬이 끝났기 때문에 건드릴 필요가 없다.
# 그런 식으로 과정을 반복함.
for i in range(len(num_list)-1) :
    for j in range(len(num_list)-1-i) :
        if num_list[j] > num_list[j+1] : 
            num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

for n in num_list :        
    print(n)