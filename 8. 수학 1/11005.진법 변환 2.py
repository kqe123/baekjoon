# 11005. 10진법 수 N이 주어진다. 이 수를 B진법으로 바꿔 출력하는 프로그램을 작성하시오.
# 10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.
# A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35
import string
N, radix = map(int, input().split())
digits = string.digits + string.ascii_uppercase  # '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def to_base(n, base):
    if not (2 <= base <= 36):
        raise ValueError("지원하는 진법은 2진수부터 36진수까지입니다.")
    
    if n == 0:
        return '0'
    
    result = ''
    while n:
        n, r = divmod(n, base)
        result = digits[r] + result
    return result
print(to_base(N,radix))

