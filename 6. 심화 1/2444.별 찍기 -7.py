# 2444. 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요. (다이아몬드)

N = int(input())
for i in range(1,N+1) :
    print(" "*(N-i) + "*"*(2*i-1))
for i in range(N-1, 0, -1) :
    print(" "*(N-i) + "*"*(2*i-1))