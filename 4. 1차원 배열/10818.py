#10818
#N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

#방법1 : max, min 없이 구하기
T = int(input())
num = list(map(int, input().split()))
maximum = 0 
minimum = 0
for i in range(T) :
    if i == 0 : 
        maximum = num[i]
        minimum = num[i]
    else : 
        if maximum < num[i] : maximum = num[i]
        if minimum > num[i] : minimum = num[i]
print(minimum,maximum)


#방법2 : max, min로 구하기
T = int(input())
num = list(map(int, input().split()))
print(min(num),max(num))
