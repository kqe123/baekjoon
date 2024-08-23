#3052
#두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 
# 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다. 
#수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 
#그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

import sys
num = []
for i in range(10) :
    value = int(sys.stdin.readline().rstrip())%42
    if value not in num :
        num.append(value)
print(len(num))

#해결법 : 중복을 빼고 몇개있는지 세는 것이므로 중복자체를 허용안하는 세트에 넣어서 갯수를
#         아는 방법도 있고, 리스트에 넣기전에 중복되는건 넣지 않게한후 갯수를 아는 방법도 있다.
