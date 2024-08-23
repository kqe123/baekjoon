#25314
#혜아는 이런 생각이 들었다. “int 앞에 long을 하나씩 더 붙일 때마다 
#4바이트씩 저장할 수 있는 공간이 늘어나는 걸까? 그럼 long long long long int는 
#16바이트까지 저장할 수 있는 정수 자료형일 거야!”
#혜아가 N바이트 정수까지 저장할 수 있다고 생각해서 칠판에 쓴 정수 자료형의 이름은 무엇일까?

N = int(input())
num = N//4
print("long "*num + "int")


#tip : 문자열 반복은 *로 하면된다. ex): print("long"*3) -> long long long
