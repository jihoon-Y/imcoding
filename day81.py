# 03. random모듈

# 스탠다드 라이브러리에 있는 random 모듈은 랜덤으로 숫자를 생성하는 다양한 함수들을 제공한다

import random
# randint() 함수
# randint() 함수는 두 수 사이의 어떤 랜덤한 정수를 리턴하는 함수이다
# randint(a, b)를 하면, a ≤ N ≤ b를 만족하는 어떤 랜덤한 정수 N을 리턴한다

import random

print(random.randint(1, 20))
print(random.randint(1, 20))
print(random.randint(1, 20))
print(random.randint(1, 20))
print(random.randint(1, 20))

# 1 이상 20 이하의 수 다섯 개를 출력하는데, 보다시피 매번 다른 랜덤한 수가 출력된다

# 스탠다드 라이브러리에 있는 random 모듈은 랜덤으로 숫자를 생성하는 다양한 함수들을 제공한다


# uniform() 함수
# uniform() 함수는 두 수 사이의 랜덤한 소수를 리턴하는 함수이다
# randint() 함수와 다른 것은 리턴하는 값이 정수가 아니라 소수라는 점이다
# uniform(a, b)를 하면, a ≤ N ≤ b를 만족하는 어떤 랜덤한 소수 N을 리턴한다

import random

print(random.uniform(0, 1))
print(random.uniform(0, 1))
print(random.uniform(0, 1))
print(random.uniform(0, 1))
print(random.uniform(0, 1))

# 0 이상, 1 이하의 수 다섯 개를 출력하는데, 매번 다른 랜덤한 수가 출력된다