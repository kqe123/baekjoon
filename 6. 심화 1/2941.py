#2941
#예를 들어, ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다. 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
#dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다. lj와 nj도 마찬가지이다. 위 목록에 없는 알파벳은 한 글자씩 센다.

words = ["c=","c-","dz=","d-","lj","nj","s=","z="]
value = input()
result = 0

#리스트에 있는 문자열이 있는지 센다음 있다면 해당 문자열을 *처리한다.
for word in words :  
    if value.count(word) > 0 :
        result += value.count(word)
        value = value.replace(word,"*")

#*처리안된 나머지 문자를 세야되니 *를 제거후 센다.
value = value.replace("*","")
result += len(value)
print(result)