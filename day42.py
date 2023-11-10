# 추상화 13. 파이썬 스타일 가이드(PEP8)

# 1. 이름 규칙
# 1-1. 모든 변수와 함수 이름은 소문자, 여러 단어일 경우 _로 나눈다

# bad
someVariableName = 1
SomeVariableName = 1

def someFunctionName():
    print("Hello")

# good
some_variable_name = 1

def some_function_name():
    print("Hello")


# 1-2. 모든 상수는 대문자로, 여러 단어일 경우 _로 나눈다

# bad
someConstant = 3.14
SomeConstant = 3.14
some_constant = 3.14

# good
SOME_CONSTANT = 3.14


# 1-3. 의미 있는 이름(변수)

# bad (의미 없는 이름)
a = 2
b = 3.14
print(b * a * a)

# good (의미 있는 이름)
radius = 2
PI = 3.14
print(PI * radius * radius)


# 1-4. 의미 있는 이름(함수)

# bad (의미 없는 이름)
def do_something():
    print("Hello, world!")

# good (의미 있는 이름)
def say_hello():
    print("Hello, world!")



# 2. 화이트 스페이스
# 2-1. 들여쓰기
# 들여쓰기는 무조건 스페이스 4개를 사용한다

# bad (스페이스 2개)
def do_something():
  print("Hello, world!")

# bad (스페이스 8개)
i = 0
while i < 10:
        print(i)

# good (스페이스 4개)
def say_hello():
    print("Hello, world!")



# 3. 함수 정의
# 함수 정의 위아래로 빈 줄이 두 개씩 있어야 한다
# 하지만 파일의 첫 줄이 함수 정의인 경우, 해당 함수 안에는 빈 줄이 없어도 된다

# bad
def a():
    print('a')
def b():
    print('b')

def c():
    print('c')

# good
def a():
    print('a')


def b():
    print('b')


def c():
    print('c')



# 4. 띄어쓰기
# 4-1. 괄호 안
# 괄호 안은 띄어쓰기를 하지 않는다

# bad
spam( ham[ 1 ], { eggs: 2 } )

# good
spam(ham[1], {eggs: 2})


# 4-2. 함수 괄호

# bad
def spam (x):
    print (x + 2)


spam (1)

# good
def spam(x):
    print(x + 2)


spam(1)


# 4-3. 쉼표
# 쉼표 앞에는 띄어쓰기를 하지 않는다

# bad
print(x , y)

# good
print(x, y)


# 4-4. 지정 연산자
# 지정 연산자 앞뒤로 띄어쓰기를 하나씩 넣는다

# bad
x=1
x    = 1

# good
x = 1


# 4-5. 연산자
# 기본적으로 연산자 앞뒤에는 띄어쓰기를 하나씩 넣는다

# bad
i=i+1
submitted +=1

# good
i = i + 1
submitted += 1


# 그러나 연산의 우선 순위를 강조할 때는 연산자 앞뒤로 붙이는 것을 권장한다
# bad
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)

# good
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)


# 4-6. 코멘트
# 일반 코드와 같은 줄에 코멘트를 쓸 경우, 코멘트 앞에 띄어쓰기를 최소 두 번 한다

# bad
x = x + 1# 코멘트

# good
x = x + 1  # 코멘트
