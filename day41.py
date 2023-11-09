# 추상화 12. 스타일
# 이해하기 쉬운 코드 = 좋은 스타일을 가진 코드

# 안 좋은 스타일의 코드 예시
print(6.28*4)
print(3.14*4*4)
print(6.28*8)
print(3.14*8*8)
# 가독성이 떨어져, 프로그램의 목적도 모르겠고 숫자들이 뭘 의미하는지 알 수가 없다
# 이 프로그램의 목적은 원의 둘레, 원의 넓이를 구하는 것이다

# 좀 더 좋은 스타일의 코드로 바꿔보았다
a = 3.14 # 원주율(파이)
b = 4 # 반지름
print(2*a*b)
print(a*b*b)
b = 8 # 반지름
print(2*a*b)
print(a*b*b)
# 이전보다 좀 더 눈에 잘 들어오지만, 여전히 무엇을 원하는 건지는 잘 알 수 없다
# 코멘트를 달면 이해가 좀 더 쉬워질 것 같다

# 보다 좋은 스타일의 코드로 바꿨다
PI = 3.14

radius = 4
print(2 * PI * radius)
print(PI * radius * radius)

radius = 8
print(2 * PI * radius)
print(PI * radius * radius)
# 변수 이름만 봐도 어떤 걸 구하려고 하는지 알 수 있어졌다
# 그러나 여기서 pi는 절대 변하지 않을 상수에 속한다
# 따라서 대문자로 바꾸고 변수의 가짓수를 줄이면 좋다
# 처음에 비해서는 많이 좋아졌지만, 연산식 만으로는 한번에 이해하게 만들기 쉽지 않다

# 함수를 사용한 깔끔한 스타일의 코드로 바꿔봤다
PI = 3.14

# 반지름이 r인 원의 둘레 계산
def calculate_circumference(r):
    return 2 * PI * r


# 반지름이 r인 원의 넓이 계산
def calculate_area(r):
    return PI * r * r


radius = 4 # 반지름
print(calculate_circumference(radius))
print(calculate_area(radius))

radius = 8 # 반지름
print(calculate_circumference(radius))
print(calculate_area(radius))