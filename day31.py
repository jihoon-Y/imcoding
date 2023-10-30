# 추상화 01. 지정 연산자
name = "지훈"

x = 7

x = x + 1
# 파이썬에서 =는 '지정 연산자'라고, 오른쪽의 값을 왼쪽 변수에 넣으라는 의미이다
# 일단 지정 연산자가 있으면 오른쪽을 먼저 보면 된다


# 추상화 02. 함수의 실행 순서
# 예시1
def hello():
    print("Hello!")
    print("Welcome to Home!")
# 함수를 정의했지만, 실행된 건 아니다 어떤 일이 일어나지 않았다

print("함수 호출 전")
hello() # hello 함수를 실행(호출)하라는 뜻이다
print("함수 호출 후")

# 예시2
def square(x):
    return x * x

print("함수 호출 전")
print(square(3) + square(4))
print("함수 호출 후")