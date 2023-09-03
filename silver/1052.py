n,k = map(int,input().split())
value = 1
left = []
while n != 1 :
    if n % 2 == 1 : 
        left.append(value)
    n //= 2
    value *= 2
left.append(value)
left.sort(reverse=True)
if len(left) <= k : 
    result = 0
else : 
    result = left[k-1] - sum(left[k:])
print(result)