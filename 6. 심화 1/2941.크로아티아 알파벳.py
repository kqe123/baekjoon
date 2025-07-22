# 2941. 예를 들어, ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다. 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
# dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다. lj와 nj도 마찬가지이다. 위 목록에 없는 알파벳은 한 글자씩 센다.

word = input()
counts = 0
croatia_words = ["c=","c-","dz=","d-","lj","nj","s=","z="]

for crotia_word in croatia_words :
    if crotia_word in word :
        counts += word.count(crotia_word)
        word = word.replace(crotia_word,"_")
    
for char in word : 
    if char != "_" :
        counts += 1
print(counts)