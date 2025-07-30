# 1018. 보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 당연히 8*8 크기는 아무데서나 골라도 된다.
# 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.
import sys
N, M = map(int, input().split())
chess = []
result = 65
right1 = "WBWBWBWB"
right2 = "BWBWBWBW"

for i in range(N) :
    chess.append(sys.stdin.readline().rstrip())

for x in range(0,N-8+1) :
    for y in range(0, M-8+1) :
        # 1. 8x8크기로 잘라내기
        cut_board = [row[y:y+8] for row in chess[x:x+8]]
        result1 = 0 
        result2 = 0

        # 2. 올바른 체스판 두개 중 최소로 바꿔야할 정사각형 개수를 구함.
        # 첫번째 줄이 WBWBWBWB여야 하는 경우
        for i in range(8) :
            for j in range(8) :
                if i % 2 == 0 and cut_board[i][j] == right1[j] :
                    continue
                elif i % 2 != 0 and cut_board[i][j] == right2[j] :
                    continue
                else : 
                    result1 += 1
        
        # 첫번째 줄이 BWBWBWBW여야 하는 경우
        for i in range(8) :
            for j in range(8) :
                if i % 2 == 0 and cut_board[i][j] == right2[j] :
                    continue
                elif i % 2 != 0 and cut_board[i][j] == right1[j] :
                    continue
                else : 
                    result2 += 1
        
        # 3. 두 결과 중 수가 적은 결과와 result를 비교함.
        if result > min(result1, result2) :
            result = min(result1,result2)

print(result)