# 추상화 09. 변수의 scope(변수가 사용 가능한 범위)

def my_function():
    x = 3
    print(x)


my_function()
# print(x) 실행하면 name 'x' is not defined라는 오류가 난다
# x라는 이름이 정의된 적 없다는 뜻이다
# x = 3이라는 건 my_function 함수 내에서만 정의가 되는 것이다
# 이걸 로컬 변수라고 한다 함수 내에서만 사용되는 변수다
# 함수 밖에서의 print(x)는 정의된 x가 없기 때문에 오류가 나는 것이다

x = 2 # 이렇게 함수 밖에서도 변수를 지정해주면 된다
# 이걸 글로벌 변수라고 한다
def my_function():
    x = 3
    print(x)


my_function()
print(x)


# 파라미터도 로컬 변수에 속한다
def square(x):
    return x * x


print(square(5))