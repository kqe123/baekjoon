# 2562. 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
# 예를 들어, 서로 다른 9개의 자연수 3, 29, 38, 12, 57, 74, 40, 85, 61이
# 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.
import sys
num_list = []
maximum = 0
pos = -1

for i in range(9) :
    num_list.append(int(sys.stdin.readline().rstrip()))

for i, num in enumerate(num_list) :
    if maximum < num :
        maximum = num
        pos = i+1

print(maximum)
print(pos)