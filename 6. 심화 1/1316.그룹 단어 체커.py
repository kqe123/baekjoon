# 1316. 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고,
# kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다. 
# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.
import sys
N = int(input())
result = 0

# 1. previous_char != 현재 char & 출현한적 없는 새 문자임.
# 2. previous_char != 현재 char & 출현한적 있는 문자임. -> 그룹 단어 X
# 3. previous_char == 현재 char 
for _ in range(N) :
    is_group_word = True
    char_list = []
    previous_char = ""
    word = sys.stdin.readline().rstrip()
    for i in range(len(word)) :
        if previous_char != word[i] and word[i] not in char_list :
            previous_char = word[i]
            char_list.append(word[i])
        
        elif previous_char != word[i] and word[i] in char_list :
            is_group_word = False
            break
    if is_group_word :
        result += 1

print(result)