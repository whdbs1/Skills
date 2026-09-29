# 1.사칙연산

a = 5
b = 3

print(a + b) # 덧셈
print(a - b) # 뺄셈
print(a * b) # 곱
print(a ** b) # 제곱
print(a / b) # 몫
print(a // b) # 목에서 정수값만
print(a % b) # 나머지

# 2.문자열(주석)

# 문자열을 만들려면 ',",''',"""을 써야함
"hello world"
'hello world'
"""hello world"""
'''hello world'''
'print(hello world)' # 잘못된 예
print("hello world") # 옳은 예

#문자열 사이에 '를 써야하면 "를 써준다("가 들어가야 하면 ')
print("python's favorite food is perl")
print('"python is very easy" she said')

#'"를 여러번 쓰려면 표시하려는 부분 앞에 \로 표시
food = 'python\'s favorite food is perl'
say = "\"python is very easy.\"he says."
print(food)
print(say)

#여러 줄인 문자열을 변수에 대입하고 싶을 때 /n을 넣거나 위 아래로 ''',"""를 쓴다
multiline = "life is too short\nyou need python"
multiline = '''
            life is too short
            you need python
            '''
multiline = """
            life is too short
            you need python
            """

"""
이스케이프 코드
\n 문자열 안에서 줄바꿈
\t 문자열 사이에 탭 간격을 줄 때 사용
\\ 문자\를 그대로 사용할 때 사용
\' '를 표현할 때 사용
\" "를 표현할 때 사용
\r 캐리지 리턴(줄 바꾸고 현제 커서를 맨 앞으로)
\f 폼 피드(줄 바꾸고 현재 커서를 다음 줄로)
\a 벨 소리(출력할 때 '삑' 소리
\b 백스페이스
\000 널 문자

주로 사용 \n,\t,\\,\',\"
"""

#문자열 더하기 곱하기
head = "python"
tail = " is fun!"
print(head + tail)

#문자열 길이 구하기(Len 함수)
a = "life is too short"
print(len(a))


# 3.슬라이싱
"""
[n]: A에 n번째에 입력 되있는 값을 찾을 수 있음
예: A=302  A[0]=3 A[1]=0 A[2]=2
[:n]: n앞에 있는 값 전부
[n:]: n뒤에 있는 값 전부
[:]: 전체 값 A[:]=302
"""

'(문제)'
#슬라이싱을 활용하여 오타 고치기
a= "pithon"
print(a[:1] + 'y' + a[2:])

#슬라이싱으로 문자열 나누기
a = "20010331Rainy"
year = a[:4]
day= a[4:8]
weather = a[8:]
print(year)
print(day)
print(weather)

#A의 값과 B의 값을 1의 자리 부터 100의 자리 까지 곱한걸 표현(백준)
A = (input())
B = (input())

print(int(A) * int(B[2]))
print(int(A) * int(B[1]))
print(int(A) * int(B[0]))
print(int(A) * int(B))

# 4.문자열 포메팅
"""
%s: 문자열
%c: 문자 1개
%d: 정수
%f: 부동소수
%o: 8진수
%x: 16진수
%%: %
"""

#숫자 바로 대입
print("I eat %d apples." %3)

#문자 바로 대입
print("I eat %s apples." %"five")

#변수로 대입
num = 4
print("I eat %d apple." %num)

#변수 2개
num = 4
date = "three"
print("I ate %d apples. so I was sick for %s days." %(num,date)






