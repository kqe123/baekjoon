#2444
#다이아몬드 형태로 별을 찍어보세요.

N = int(input())
for i in range(1,N+1) :
    print(" "*(N-i)+ "*"*(2*i-1))
for i in range(N-1,0,-1) :
    print(" "*(N-i) + "*"*(2*i-1))
