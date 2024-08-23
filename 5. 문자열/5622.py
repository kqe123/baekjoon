#5622
#상근이의 할머니는 아래 그림과 같이 오래된 다이얼 전화기를 사용한다.
#숫자 1을 걸려면 총 2초가 필요하다. 1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며, 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.
#할머니가 외운 단어가 주어졌을 때, 이 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성하시오.

take = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
word = input()
time = 0
for char in word :
    for i in range(len(take)) :
        if char in take[i] :
            time += 2 + i + 1 
print(time) 

