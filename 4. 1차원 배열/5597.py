#5597
#X대학 M교수님은 프로그래밍 수업을 맡고 있다. 교실엔 학생이 30명이 있는데, 
#학생 명부엔 각 학생별로 1번부터 30번까지 출석번호가 붙어 있다.
#교수님이 내준 특별과제를 28명이 제출했는데, 
#그 중에서 제출 안 한 학생 2명의 출석번호를 구하는 프로그램을 작성하시오.

import sys
sub = []
not_sub = []
for i in range(28) :
    sub.append(int(sys.stdin.readline().rstrip()))

for i in range(1,31) :
    if i not in sub :
        not_sub.append(i)
not_sub.sort()

for i in range(len(not_sub)) :
    print(not_sub[i])

#list.sort() : 해당 리스트를 오름차순으로 정렬, 반환값으로 쓰면 None이 나옴. reverse=True로 내림차순 정렬 가능
#sorted(list): 해당 리스트가 실제로 정렬되진않고 반환값으로 오름차순으로 정렬된 해당 리스트가 나옴.
#              마찬가지로 reverse=True로 내림차순도 가능
