# 6-3. while
# = 또다른 반복문

customer = "지훈"
index = 5
# # while (조건): 이런 형태로 입력한다
while index >= 1: # index가 1이 될 때까지 반복하라는 명령
    print("{0}님, 주문하신 음료 나왔습니다. {1} 번 남았어요.".format(customer, index))
    index -= 1 # index를 1씩 줄여가라는 명령
    if index == 0:
       print("음료는 폐기되었습니다.") # 이러고 while 반복문 탈출한다


customer = "승용"
index = 1
while True:
    print("{0}님, 주문하신 음료 나왔습니다. 호출 {1}회째 입니다".format(customer, index))
    index += 1 # 무한 루프에 빠짐 이럴 때는 ctrl+c 누르면 종료됨

customer = "승용"
person = "Unknown"

while person != customer :
    print("{0}님, 주문하신 음료 나왔습니다".format(customer))
    person = input("이름이 어떻게 되세요? ") # 조건이 맞을 때까지 input 반복, 맞으면 종료