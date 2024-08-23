#1546
#세준이는 기말고사를 망쳤다. 세준이는 점수를 조작해서 집에 가져가기로 했다. 일단 세준이는 자기 점수 중에 최댓값을 골랐다. 이 값을 M이라고 한다. 그리고 나서 모든 점수를 점수/M*100으로 고쳤다.
#예를 들어, 세준이의 최고점이 70이고, 수학점수가 50이었으면 수학점수는 50/70*100이 되어 71.43점이 된다.

T = int(input())
grade = list(map(int, input().split()))
best = max(grade)
for i in range(T) :
    grade[i] = grade[i]/best*100

print(sum(grade)/T)

#sum(list) : 리스트 요소의 합계 반환