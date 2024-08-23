#1157
#알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
#단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

word = input()
counts = {}
for char in word : 
    if char.upper() in counts : 
        counts[char.upper()] += 1
    else : 
        counts[char.upper()] = 1

maxcount = max(counts.values())
result = "" 
for key in counts :
    if counts[key] == maxcount and result == "" :
        result = key
    elif counts[key] == maxcount and result != "" :
        result = "?"
        break
print(result)

#dict.keys() : 해당 딕셔너리의 키 집합을 반환함(형변환 필요)
#dict.values() : 해당 딕셔너리의 값 집합을 반환함(형변환 필요)
