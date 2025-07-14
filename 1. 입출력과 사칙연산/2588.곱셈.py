# 2588. (1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.
a = int(input())
b = int(input())
result1 = a * (b%10)
result2 = a * (b%100//10)
result3 = a * (b//100)
result4 = result1 + 10*result2 + 100*result3
print(result1, result2, result3, result4, sep="\n")