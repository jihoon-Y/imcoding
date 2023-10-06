# 6-1. if
# = 분기, 이런 상황에서는 이런 코드를, 저런 상황에서는 저런 코드를 사용하게끔 하는 기능

weather = "비"
# if 조건:
#     실행 명령문 <ㅡ기본적으로 이런 형태를 취한다

if weather == "비": # 변수가 맞게 들어가면
    print("우산을 챙기세요") # 명령문이 잘 출력된다

if weather == "맑음": # 변수가 맞지 않게 들어가면
    print("우산을 챙기세요") # 명령문이 출력되지 않는다

# # 한 가지 조건이 아닌 두 가지 조건을 설정하고 싶을 때
weather = "맑음"
if weather == "비":
    print("우산을 챙기세요")
    
elif weather == "미세먼지": # 두 번째 조건을 설정할 때 쓴다
    print("마스크를 챙기세요")

else: # 지정된 조건 외 모든 상황에 출력된다
    print("준비물 필요 없어요")


weather = input("오늘 날씨는 어때요? ")
# 프로그램을 조금 더 매끄럽게 하기 위해 input을 사용할 수 있다
# input은 직접 사용자에게 입력을 받는 문장이다
# 이때 입력한 값은 str형태로 변수에 저장된다
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요")

temp = int(input("기온은 어때요? "))
# int로 감싸면 사용자가 입력한 정수 값을 변수에 저장한다
if 30 <= temp:
    print("너무 더워요 나가지 마세요")
#elif 10 <= temp < 30: # 이런 식으론 안되나?
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요")
elif 0<=  temp < 10: # 뭐야 되네
    print("쌀쌀해요 옷을 잘 챙겨입으세요")
else:
    print("너무 추우니 절대 나가지 마세요")


# 6-2. for
# = 반복문

print("대기번호 : 1") # 1, 2, 3,... 수동으로 입력할 수 없을만큼 수가 커질 때 쓴다

for waiting_no in [0, 1, 2, 3, 4]: # 변수에 대입될 값들이 모두 출력될 때까지 반복
    print("대기번호 : {0}".format(waiting_no)) # 여기서도 문자열포맷이 쓰인다

# for waiting_no in range[1:50]: # 이건 왜 안되는거지
#     print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(10): # 랜덤에서의 randrange와 비슷하다
#     # 0, 1, 2, ... , 9 까지이다 10 미만
#     # 맞게 쓰려면 콜론이 아니라 콤마를 써야했다 range(1, 51) 51미만 까지니까
    print("대기번호 : {0}".format(waiting_no))

starbucks = ["지훈", "병선", "유빈"]
for customer in starbucks: # 손님을 새로운 변수로 지정하고 스벅 안의 값들을 출력한다
    print("{0}님, 주문하신 음료 나왔습니다.".format(customer))
    # 지훈, 병선, 유빈이 들어있는 스타벅스에서 하나씩 돌아가며 커스터머에 대입/출력
# 그러니까 이건 변수가 크게 변하지 않는 상황에서 단순반복을 위한 기능인 것이다