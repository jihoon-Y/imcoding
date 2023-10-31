# 추상화 03. return문 제대로 이해하기
# return = (함수가) 무언가를 돌려주는 것
# 역할 두 가지 : 값 돌려주기, 함수 즉시 종료하기

def square(x):
    print("함수 시작")
    return x * x
    print("함수 끝") # return이 함수를 종료하기 때문에 절대 출력될 일 없는 명령어
    # = Dead code(의미 없는 코드)


print(square(3))
print("Hello World!")

# 추상화 04. return과 print의 차이

def print_square(x): # print는 파라미터 x의 제곱을 '출력'해주는 함수
    print(x * x) 


def get_square(x): #get은 파라미터 x의 제곱을 '리턴'해주는 함수
    return x * x


print_square(3) # 9가 출력됨
get_square(3) # 9가 리턴되지만 출력은 안되고 프로그램이 끝남
print(get_square(3)) # 리턴된 9가 출력됨
print(print_square(3)) # print문에는 return이 없으므로 리턴값도 없다
# 파이썬에서는 사실 리턴문이 따로 없으면 리턴값이 없다는 의미인 None이라는 값이 리턴된다
# 그러면 함수 호출 부분이 None이라는 값으로 대체된다 따라서 None이 출력된다


# 추상화 05. return과 print의 차이 실습
def first():
    message = "코드잇"
    return message

def second():
    message = "codeit"
    print(message)


def third():
    message = None
    print(message)


# 테스트 코드
print(first())
second()
print(third()) 
# third()함수를 호출하면 함수 본문이 실행된다
# print(message)에 의해 None이 한 번 출력된다
# 그리고 함수에 return이 없으므로 None이 호출한 결괏값으로 반환된다
# 그래서 None이 두 번 출력되는 것이다

# 함수는 호출된 후 항상 값을 반환한다 / return문에 반환할 값이 명시되지 않으면 None을 반환한다

# 반환할 값을 명시했을 때
def return_message():
    return "안녕하세요"


return_message()
# 반환할 값을 명시할 때 return문을 사용한다
# return_message() 함수를 호출하면 반환하도록 명시한 "안녕하세요"라는 문자열을 함수 호출한 자리로 돌려준다

# 반환할 값을 명시하지 않았을 때
def return_nothing():
    message = "안녕하세요"


return_nothing()
# 위 코드에는 값을 반환하기 위한 return문이 없다. 이런 경우 None을 함수를 호출한 자리로 돌려준다

def return_nothing():
    return


return_nothing()
# 위 코드에서는 return문이 쓰였지만 반환할 값이 명시되어 있지 않다 이때도 None을 반환한다