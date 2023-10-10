# 7-1. 함수
# =박스

def open_account():
    print("새로운 계좌가 생성되었습니다.")
    # 함수는 정의만 되었지, 실제로 호출하기 전까지는 실행이 되지 않는다

open_account() # 이렇게 정의를 해줘야만 함수가 호출되어 실행된다
# 그래서 이게 뭐라는거지..? 그냥 전달만 하는 건가?



# 7-2. 전달값과 반환값
def open_account():
    print("새로운 계좌가 생성되었습니다.")

# 입금하는 함수
def deposit(balance, money): #입금한 함수에는 잔액과 입금하려는 금액 다 전달받아서 원하는 값 반환
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance+money))
    return balance+money # 반환할 때는 return을 사용하면 된다.

balance = 0 # balance(잔액)라는 변수를 0원이라고 지정했는데
balance = deposit(balance, 1000) # deposit 함수를 사용해 잔액에 1000을 더하는 새로운 변수로 지정한 것이다
print(balance)

# 출금하는 함수
def withdraw(balance,money):
    if balance >= money: #잔액이 출금액보다 많은 경우
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance-money))
        return balance-money
    else: # 잔액이 출금액보다 적은 경우
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance

balance = 0 #잔액
balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
balance = withdraw(balance, 500)


def withdraw_night(balance, money): # 저녁에 출금
    commission = 100 # 수수료 100원
    return commission, balance-money-commission # 튜플형식?
# 받고 싶은 값 = 수수료와 잔고에서 출금하고 남은 잔액을 튜플 형식으로
# 이전까지는 return에서 하나의 값을 보냈는데, 이번엔 콤마 형식으로 반환된다

balance = 0 #잔액
balance = deposit(balance, 1000)
commission, balance = withdraw_night(balance, 500)
print("수수료는 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))



# 7-3. 기본값

def profile(name, age, main_lang):
    print("이름 : {0}\n나이 : {1}\n주사용언어 : {2}"\
          .format(name, age, main_lang)) # 코드 중에 \를 입력하면 줄바꿈 가능, 하나의 문장으로 인식

profile("지훈", 30, "파이썬")
profile("승용", 28, "자바")

# 위 상황에서 같은 나이, 같은 언어를 사용한다고 가정해보자
# 같은 내용을 매번 입력할 필요 없기 때문에 같은 값으로 통일할 수 있는 것이 기본값이다
# 근데 그럼 print문장에 직접 입력하면 안 되는 건가? 왜 굳이 함수의 기본값으로 쓰지

def profile(name, age=20, main_lang="파이썬"):
    print("이름 : {0}\n나이 : {1}\n주사용언어 : {2}"\
          .format(name, age, main_lang))
# 함수가 호출될 때 전달받은 값이 없으면 기본값이 호출된다고 한다. 그냥 print문과는 쓰임이 조금 다른 듯

profile("지훈", "자바") # ??이렇게 하면 안되네
profile("승용")