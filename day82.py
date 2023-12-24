# 04. datetime 모듈

# 스탠다드 라이브러리에 있는 이 모듈은 날짜와 시간을 다루기 위한 다양한 클래스를 갖추고 있다
# '클래스' 개념은 아직 배우지 않았지만, 일단은 몰라도 이 모듈을 사용하는 데에는 문제없다

# 1. datetime 값 생성
# 2020년 3월 14일을 파이썬으로 표현해보자

import datetime

pi_day = datetime.datetime(2020, 3, 14)
print(pi_day)
print(type(pi_day))

# 출력해보니 시간은 자동으로 00시 00분 00초로 설정되어 있는데, 시간까지도 직접 정할 수 있다

pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
print(pi_day)
print(type(pi_day))


# 2. 오늘 날짜
# 우리가 정해준 날짜와 시간이 아닌, 코드를 실행한 '지금 이 순간'의 날짜와 시간을 받아올 수도 있다

today = datetime.datetime.now()
print(today)
print(type(today))


# 3. timedelta 타입
# 두 datetime 값 사이의 기간을 알고 싶을 때는, 마치 숫자 뺄셈을 하듯이 그냥 빼면 된다

today = datetime.datetime.now()
pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
print(today - pi_day)
print(type(today - pi_day))


# 두 datetime 값을 빼면, timedelta라는 타입이 나온다
# 이건 날짜 간의 차이를 나타내는 타입이라고 생각하면 된다

# 반대로 timedelta를 생성해서 datetime 값에 더할 수도 있다

today = datetime.datetime.now()
my_timedelta = datetime.timedelta(days=5, hours=3, minutes=10, seconds=50)

print(today)
print(today + my_timedelta)


# 4. datetime 해부하기
# datetime 값에서 연도나 월 같은 값을 추출할 수도 있다

today = datetime.datetime.now()

print(today)
print(today.year)  # 연도
print(today.month)  # 월
print(today.day)  # 일
print(today.hour)  # 시
print(today.minute)  # 분
print(today.second)  # 초
print(today.microsecond)  # 마이크로초


# 5.datetime 포매팅
# datetime 값을 출력하면 별로 예쁘지 않은데, strftime() 함수를 사용하면 취향껏 바꿀 수 있다

today = datetime.datetime.now()

print(today)
print(today.strftime("%A, %B %dth %Y"))
