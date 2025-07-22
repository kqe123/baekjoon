# 25206. 인하대학교 컴퓨터공학과를 졸업하기 위해서는, 전공평점이 3.3 이상이거나 졸업고사를 통과해야 한다. 그런데 아뿔싸, 치훈이는 깜빡하고 졸업고사를 응시하지 않았다는 사실을 깨달았다!
# 치훈이의 전공평점을 계산해주는 프로그램을 작성해보자.
import sys
grade_list = {
    "A+" : 4.5, "A0" : 4.0, "B+" : 3.5,
    "B0" : 3.0, "C+" : 2.5, "C0" : 2.0,
    "D+" : 1.5, "D0" : 1.0, "F" : 0.0
}
total_credit = 0
result = 0

while True :
    value = sys.stdin.readline().rstrip()
    if value == "" :
        break

    _ ,credit, grade = value.split()
    if grade == "P" :
        continue
    else : 
        credit = float(credit)
        total_credit += credit
        result += (credit*grade_list[grade])

print(result/total_credit)