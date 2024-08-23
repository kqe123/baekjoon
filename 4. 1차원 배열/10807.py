#10807
#총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.

T = int(input())
numbers = list(map(int, input().split()))
want = int(input())
print(numbers.count(want))


#리스트.count(X) : X의 개수를 반환함.
