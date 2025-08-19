# 1181. 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로
# 단, 중복된 단어는 하나만 남기고 제거해야 한다.

import sys
T = int(input())
words = {}
for i in range(T) :
    word  = sys.stdin.readline().rstrip()
    if len(word) in words :
        if word not in words[len(word)] : 
            words[len(word)].append(word)
    else : 
        words[len(word)] = [word]

for key in sorted(words) :
    for value in sorted(words[key]) :
        print(value)


