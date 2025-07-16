# 10818. N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
N = int(input())
num_list = list(map(int, input().split()))
maximum = 0
minimum = 0

for i, num in enumerate(num_list) :
    if i == 0 :
        maximum = num
        minimum = num
    if maximum < num :
        maximum = num
    if minimum > num :
        minimum = num

print(minimum, maximum)
