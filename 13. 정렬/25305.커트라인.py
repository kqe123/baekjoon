# 25305. 2022 연세대학교 미래캠퍼스 슬기로운 코딩생활에 N명의 학생들이 응시했다.
# 이들 중 점수가 가장 높은 k명은 상을 받을 것이다. 이 때, 상을 받는 커트라인이 몇 점인지 구하라.

n, k  = map(int, input().split())
num_list = list(map(int, input().split()))

# 버블 정렬
for i in range(len(num_list)-1) :
    for j in range(len(num_list)-i-1) :
        if num_list[j] < num_list[j+1] :
            num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

print(num_list[k-1])

