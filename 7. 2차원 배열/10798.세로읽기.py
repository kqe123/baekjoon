# 10798. 한 줄의 단어는 글자들을 빈칸 없이 연속으로 나열해서 최대 15개의 글자들로 이루어진다.
# 또한 만들어진 다섯 개의 단어들의 글자 개수는 서로 다를 수 있다. 
# 심심해진 영석이는 칠판에 만들어진 다섯 개의 단어를 세로로 읽으려 한다.
# 세로로 읽을 때, 각 단어의 첫 번째 글자들을 위에서 아래로 세로로 읽는다. 다음에 두 번째 글자들을 세로로 읽는다. 이런 식으로 왼쪽에서 오른쪽으로 한 자리씩 이동 하면서 동일한 자리의 글자들을 세로로 읽어 나간다. 위의 그림 1의 다섯 번째 자리를 보면 두 번째 줄의 다섯 번째 자리의 글자는 없다. 이런 경우처럼 세로로 읽을 때 해당 자리의 글자가 없으면, 읽지 않고 그 다음 글자를 계속 읽는다. 그림 1의 다섯 번째 자리를 세로로 읽으면 D1gk로 읽는다. 

import sys
table = []
max_column = 0
# 1, 테이블 생성
for _ in range(5) :
    table.append(sys.stdin.readline().rstrip())

# 2. 가장 긴 단어의 문자 개수를 센다.
for i in range(5) :
    if max_column < len(table[i]) :
        max_column = len(table[i])

# 3. 세로로 2차원 배열을 순회하되,
# 현재 선택한 열이 현재 행의 열의 개수의 범위를 벗어나면 skip
for j in range(max_column) :
    for i in range(5) :
        if len(table[i])-1 < j :
            continue
        print(table[i][j],end="")
