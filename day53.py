# 제어문12. 우승 상금 투자

# 1988년 쌍문동에 사는 택이는 바둑 대회 우승 상금으로 5,000만 원을 받았다

# 이 돈을 어떻게 할지 , 이웃인 동일 아저씨와 미란 아주머니의 의견 중 하나를 선택하려 한다

# 동일 아저씨 의견
# > 원금에 붙은 이자에 다시 이자가 붙는 연복리 예금에 넣기


#  <연복리 예금 상품 정보>

#  원금: 50,000,000 원
#  연 이율: 12%
#  1년 뒤 은행 잔고: 50,000,000 * (1 + 12%) = 56,000,000 원
#  2년 뒤 은행 잔고: 50,000,000 * (1 + 12%) * (1 + 12%) = 62,720,000 원
#  ...


# 미란 아주머니 의견
# > 아파트 가치 상승을 고려하여 당시 매매가 5000만 원인 은마 아파트 사기

# 2016년 기준 은마아파트의 매매가는 11억 원.
# 1988년 은행에 5,000만 원을 넣었을 경우 2016년에는 얼마가 있을지 계산하여,

# 은행에 저축해 둔 금액이 더 크면, *원 차이로 동일 아저씨 말씀이 맞습니다.를 출력하고
# 은마아파트의 가격이 더 크면, *원 차이로 미란 아주머니 말씀이 맞습니다.를 출력하는 코드를 작성하라

# 조건1
# 금액은 정확한 표기를 위해 아래 값을 복사해서 이용하시는 걸 권장한다
# 1100000000
# 50000000    

# 조건2
# 2016년에 은행에 저축해 둔 금액 계산은 while 문을 이용한 반복문으로 계산하라

# 조건3
# 은마아파트 가격과 은행에 저축해 둔 금액을 비교 후 메시지 출력시에는 if 문을 사용하라

# 조건4
# 최종 결과에서 1원 미만은 계산하지 않는다



# 풀이

# 1. 상수, 변수 고정
# 먼저 이 프로그램에서 사용될 상수와 변수를 모두 정의해보자
# 사용될 값들을 미리 적어 두면 틀이 잡힌 상태에서 고민을 시작할 수 있다
# 상수(바뀌지 않을 값)와 변수(바뀔 값)를 나눠서 생각해보자
# 상수 이름은 모두 대문자로 쓴다는 점 잊지 말자. 먼저 상수는 어떤 것들이 있을까?

# 이자율 (INTEREST_RATE): 12%로 고정
# 2016년 은마아파트 가격 (APARTMENT_PRICE_2016): 11억 원으로 고정.

# 2. 상수 정의
INTEREST_RATE = 0.12
APARTMENT_PRICE_2016 = 1100000000

# 우선 반복문을 돌기 위해 사용되는 변수를 생각해 보자
# 우리는 1988년부터 시작해서 2016년까지 반복을 해야 하는데
# 그러면 연도를 나타내는 변수가 필요하므로 year라고 이름을 짓자
# 또 어떤 변수가 필요할까? 처음에는 은행에 5,000만 원을 넣었지만, 매년 그 금액이 바뀔 텐데
# 이건 bank_balance라는 변수에 저장하자

# 연도 (year): 1988부터 2016까지 바뀜
# 은행 잔액 (bank_balance): 50000000으로 시작해서 매년 이자가 쌓임

# 3. 변수 정의
year = 1988
bank_balance = 50000000

# 팁! (Python 3.6 버전 이상) 숫자를 천 단위로 나누고 싶을 때 underscore 를 쓸 수 있다
# APARTMENT_PRICE_2016 = 1_100_000_000
# bank_balance = 50_000_000

# 4. while 반복문
# 반복문을 이용해서 1988년부터 2016년까지 돈이 얼마나 쌓이는지 계산해야 한다
# 어떻게 할 수 있을까?
# while 반복문의 수행 부분에 들어갈 때마다 bank_balance가 12%씩 늘어나도록 하면 된다

bank_balance = bank_balance * (1 + INTEREST_RATE)

# 5. 그런데 수행 부분에 몇 번이나 들어가야 할까?
# 1988년에서 1989년으로 넘어갈 때 이자가 쌓여야 한다
# 마찬가지로 1989년에서 1990년으로 넘어갈 때도 이자가 쌓여야 한다
# 이런 식으로 2015년에서 2016년으로 넘어갈 때까지 수행 부분으로 들어가서 이자가 쌓여야 한다
# 그러면 반복문을 이렇게 쓸 수 있다
while year < 2016:
    bank_balance = bank_balance * (1 + INTEREST_RATE)
    year += 1

# 6. if, else문
# 마지막으로 결과를 출력하면 된다
# 은행 잔액이 더 큰지 아파트 가격이 더 큰지에 따라서 출력 결과를 정하면 된다

if bank_balance > APARTMENT_PRICE_2016:
    print("{}원 차이로 동일 아저씨 말씀이 맞습니다.".format(int(bank_balance - APARTMENT_PRICE_2016)))
else:
    print("{}원 차이로 미란 아주머니 말씀이 맞습니다.".format(int(APARTMENT_PRICE_2016 - bank_balance)))
