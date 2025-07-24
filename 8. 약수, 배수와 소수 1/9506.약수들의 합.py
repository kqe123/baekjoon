# 9506. 어떤 숫자 n이 자신을 제외한 모든 약수들의 합과 같으면, 그 수를 완전수라고 한다.
# 예를 들어 6은 6 = 1 + 2 + 3 으로 완전수이다. n이 완전수인지 아닌지 판단해주는 프로그램을 작성하라.
import sys
while True : 
    factor_list = []
    n = int(sys.stdin.readline().rstrip())
    if n == -1 :
        break

    for i in range(1,n//2+1) : 
        if n % i == 0 :
            factor_list.append(i)

    if sum(factor_list) != n :
        print(f"{n} is NOT perfect.")
    else : 
        print(f"{n} = ",end="")
        for i in range(len(factor_list)) :
            if i == len(factor_list)-1 :
                print(f"{factor_list[i]}")
            else : 
                print(f"{factor_list[i]} + ", end="")

