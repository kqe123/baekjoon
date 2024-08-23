#10951
#두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

while True : 
    try : 
        a,b = map(int,input().split())
        print(a+b)
    except : 
        break


#Tip : EOF란 End of File의 약자로 아무것도 입력하지 않고 enter를 누르게 되면 
#      EOFError가 난다. 즉 이 문제는 종결규칙이 없어 그냥 Enter를 누르면 프로그램이
#      끝날수 있게 try, except문으로 만들어야 된다.
