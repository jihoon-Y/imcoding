# 02. 스탠다드 라이브러리
# 사실 개발자가 쓸법한 함수들은 상당부분 이미 모듈로 만들어져있다
# 파이썬을 설치하면 standart library(표준 라이브러리)라는 것이 같이 딸려온다
# 이 스탠다드 라이브러리에는 쓸만한 여러 모듈들이 들어가 있다

import math

print(math.log10(100))
print(math.cos(0))
print(math.pi)


import random

print(random.random())  # 0.0~1.0사이의 랜덤 수가 출력된다


import os  # os는 operating system, 즉 운영체제의 약자이다

print(os.getlogin())
print(os.getcwd())