#25206
#20줄에 걸쳐 치훈이가 수강한 전공과목의 과목명, 학점, 등급이 공백으로 구분되어 주어진다.
#등급이 P인 과목은 계산에서 제외해야 하며, 치훈이의 전공평점을 계산해주는 프로그램을 작성해보자.
#전공평점은 전공과목별 (학점 × 과목평점)의 합을 학점의 총합으로 나눈 값이다.

import sys
Rating = {"A+" : 4.5, "A0" : 4.0, "B+" : 3.5, "B0" : 3.0, "C+" : 2.5, "C0" : 2.0, "D+" : 1.5
          ,"D0" : 1.0, "F" : 0.0}
total_credit = 0.0
total_major = 0.0
for i in range(20) :
    subject,credit,grade = sys.stdin.readline().rstrip().split()
    credit = float(credit)
    if grade == "P" : continue
    else : 
        total_major += Rating[grade] * credit
        total_credit += credit

print(total_major/total_credit)

#continue : 나머지 실행문 무시하고 반복문 조건검사로 돌아간다.
#break : 반복문 탈출한다.
