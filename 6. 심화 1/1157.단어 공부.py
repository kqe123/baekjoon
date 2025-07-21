# 1157. 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
# 단, 대문자와 소문자를 구분하지 않는다.

word = input()
used_char = {}
answer = ""
maximum = 0
for i in range(len(word)) :
    if word[i].upper() in used_char :
        used_char[word[i].upper()] += 1
    else : 
        used_char[word[i].upper()] = 1

for key in used_char :
    if used_char[key] > maximum : 
        answer = key
        maximum = used_char[key]
    elif used_char[key] == maximum : 
        answer = "?"
print(answer)