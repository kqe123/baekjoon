# 10814. 온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다.
# 이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.
import sys
N = int(input())
members = {}

# 각 age(키)에 name(값)이 가입순으로 append되기 때문에 별도의 처리는 필요 없음.
for i in range(N) :
    age, name = sys.stdin.readline().split()
    age = int(age)
    if age not in members :
        members[age] = [name]
    else : 
        members[age].append(name)

for key in sorted(members) :
    for m in members[key] :
        print(key, m)
