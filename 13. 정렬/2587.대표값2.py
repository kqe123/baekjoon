# 2587. 다섯 개의 자연수가 주어질 때 이들의 평균과 중앙값을 구하는 프로그램을 작성하시오.

num_list = []
for i in range(5) :
    num_list.append(int(input()))

for i in range(4) : 
    for j in range(len(num_list)-i-1) :
        if num_list[j] > num_list[j+1] :
            num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

print(int(sum(num_list)/5))
print(num_list[2])

