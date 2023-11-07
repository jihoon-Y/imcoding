# 추상화 11. 상수(constant)

# pi = 3.14 # 원주율 '파이', 첫 번째 변수
PI = 3.14 # 상수로 지정할 때는 모두 '대문자'로 표기하는 약속이 있다
# 굳이 이렇게 대문자로 표기하는 이유는 크게 두 가지가 있다
# 첫 번째로는 일반 변수와 구분하기 위함이다
# 두 번째로는 실수 방지를 위함이다 어떤 상황에서도 바꾸지 않겠다는 의미이기도 하다

# 반지름을 받아서 원의 넓이 계산
def calculate_area(r): # calculate_area는 원의 넓이를 계산해주는 함수
    return PI * r * r


radius = 4 # 반지름, 두 번째 변수
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))

# PI = 0 이렇게 상수도 변경할 수는 있지만, 명확히 안 좋은 코드에 속한다
radius = 6
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))

radius = 7
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))

# radius는 계속 새로운 값을 주는 반면, pi는 한 번도 바뀌지 않았고 바뀌지 않을 예정이다