#1316
#그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 
#예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만,
#aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
#단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

import sys
T = int(input())
alphabet = []
result = 0 
for i in range(T) :
    word = sys.stdin.readline().rstrip()
    pre_alpha = "" #이전 문자
    isGroup = True #그룹 단어의 여부
    for char in word : 
        if char not in alphabet : #새로운 문자인경우
            alphabet.append(char)
        elif char in alphabet and pre_alpha == char : #새 문자는 아니지만 이전문자와 연속되는 경우
            pass
        else : #새 문자도 아니고, 연속되지도 않은 경우 -> 그룹 단어가 아님
            isGroup = False
            break
        pre_alpha = char
    if isGroup == True : result += 1
    alphabet.clear()

print(result)

#해결법 : 그룹 단어인지 아닌지 구분하는법은 각 단어를 검사할때 연속되지 않으면서 기존에 나온 문자가 또 나오면 그룹 단어가 아니다.

    
