import calculator  # calculator라는 파이썬 파일을 불러오겠다는 의미이다
# 이렇게 불러와서 사용할 때는 calculator.py 파일을 모듈이라고 부른다
# 즉, 다른 파일에서 사용할 수 있는 파이썬 코드를 모듈이라 하는 것이다
# 그런데 이건 같은 폴더에 있기 때문에 쉽게 사용할 수 있는 것이다
# (다른 폴더에 있는 모듈도 불러올 수 있긴 하다)

print(calculator.add(2, 5))

print(calculator.multiply(3, 4))

# 모듈이 잘 작동하는 걸 알 수 있다
# 근데 이 모듈의 이름을 원하는 대로 바꿀 수 있다


import calculator as calc  # 이 모듈을 사용할 때 calc라고 쓰겠다고 선언

print(calc.add(2, 5))

print(calc.multiply(3, 4))


# 모듈의 이름을 바꿔보았다
# 근데 이 앞에 모듈 이름을 매번 써야하는게 좀 귀찮을 수도 있다


from calculator import add, multiply
# calculator 모듈에서 add 함수와 multiply 함수만 불러오겠다는 뜻이다
# 그러면 이제 모듈 이름을 쓸 필요가 없다
print(add(2, 5))

print(multiply(3, 4))

# 그런데 추가로 함수를 사용하고 싶으면, 맨 윗줄에 추가해야한다
# from calculator import *
# 특정 함수 대신에 *을 사용하면 모든 함수를 불러올 수 있다
# 권장하지는 않는데, 함수들의 출처를 알 수 없다는 것이다
# 그래서 필요한 함수들만 불러오거나 as calc처럼 간편화 하는 것을 추천한다