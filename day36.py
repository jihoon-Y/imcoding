# 추상화 10. scope 퀴즈
# 코드 실행 결과로 알맞은 내용을 고르자

def my_function():
    x = "코드잇"
    x = "을지로"


my_function()
# print(x)

# 오류 발생


# 코드 실행 결과로 알맞은 것을 고르자
x = 100

def my_function():
    x = 0
    print(x)


my_function()
print(x)

# 0
# 100

# 코드의 실행 결과로 알맞은 것을 고르자
x = 10

def my_function():
    y = 5
    print(x + y)


my_function()
print(x)
# 15
# 10