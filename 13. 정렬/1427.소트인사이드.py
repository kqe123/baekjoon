# 1427. 배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

a = list(map(int, input()))
for i in range(len(a)-1) :
    for j in range(len(a)-1-i) :
        if a[j] <= a[j+1] : 
            a[j], a[j+1] = a[j+1], a[j]

for i in a :
    print(i,end="")
