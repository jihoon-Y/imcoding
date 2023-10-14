# 08. format을 이용한 문자열 포매팅
# 오늘은 2023년 10월 14일입니다. 를 출력해보자
year = 2023
month = 10
day = 14
print("오늘은 {0}년 {1}월 {2}일입니다.".format(year, month, day))
# 이거로도 좋지만, 조금 더 깔끔하게도 가능하다
date_string = "오늘은 {0}년 {1}월 {2}일입니다." # 문자열을 변수로 지정하고
print(date_string.format(year, month, day)) # 그 변수에 포매팅도 가능하다

# 다음 날을 출력하고 싶다면?
date_string = "오늘은 {0}년 {1}월 {2}일입니다."
print(date_string.format(year, month, day+1))



# 09. format 다루기
print("저는 {}, {}, {}을 좋아합니다!.".format("공부", "보드게임", "외출"))
print("저는 {1}, {0}, {2}을 좋아합니다!.".format("공부", "보드게임", "외출"))
# 프로그래밍할 때는 0부터 센다

num_1 = 1
num_2 = 3
print("{0} 나누기 {1}은 {2}입니다.".format(num_1, num_2, num_1/num_2))
# 문장에 변수와 변수에 저장된 값의 연산 결과까지 넣었다
# 연산 결과를 소수점 둘째자리까지만 하고 싶다면 어떻게 할까?
print("{0} 나누기 {1}은 {2}입니다.".format(num_1, num_2, round(num_1/num_2, 2)))
# 라고 생각했고 결과도 잘 나왔지만 다른 방법이 있었다
print("{0} 나누기 {1}은 {2:.2f}입니다.".format(num_1, num_2, num_1/num_2))
# {2} 안에 :.2f를 넣는 것이다 .2는 소수점 둘째자리까지, f는 float를 뜻한다



# 10. 문자열을 포매팅하는 다양한 방식
# 10-1. 가장 오래된 방식 (% 기호)
name = "지훈"
age = 30

print("제 이름은 %s이고 나이는 %d살입니다." % (name, age))
# '포맷 스트링'이라고 부르는 이 방식은 요즘은 거의 사용되지 않지만 C나 자바 등에서 유사한 방식으로 포매팅한다

# 10-2. 2020년 기준 .format()이 가장 많이 사용되는 방식이다

# 10-3. 새로운 방식 (f-string)
name = "승용"
age = 28

print(f"제 이름은 {name}이고 {age}살입니다.")
# 파이썬 버전 3.6부터 새롭게 나온 방식이지만 좋은 평을 받고 있어 앞으로 많이 사용될 것으로 보인다



# 11. 문자열 포매팅 실습
wage = 5  # 시급 (1시간에 5달러)
exchange_rate = 1142.16  # 환율 (1달러에 1142.16원)

# "1시간에 5달러 벌었습니다." 출력
print("{0}시간에 {1}{2} 벌었습니다.".format(1, wage * 1, "달러"))

# "5시간에 25달러 벌었습니다." 출력
print("{0}시간에 {1}{2} 벌었습니다.".format(5, wage * 5, "달러"))

# "1시간에 5710.8원 벌었습니다." 출력
print("{0}시간에 {1}{2} 벌었습니다.".format(1, exchange_rate * 5, "원"))

# "5시간에 28554.0원 벌었습니다." 출력
print("{0}시간에 {1:.1f}{2} 벌었습니다.".format(5, exchange_rate * 25, "원"))



# 12. 불 대수 (수학자 조지 불의 이름을 따옴)
# 일상적인 논리를 수학적으로 표현한 것, 일상에서 사용하는 숫자와 다르게 진리값을 사용한다
# True, Flase만 사용하며 연산은 AND, OR, NOT이 있다 명제에 따라 값이 나옴

# AND 연산 : X와 Y 모두 참일 때만 True
# OR 연산 : X와 Y 중 하나라도 참이면 True
# NOT 연산 : 참이면 거짓으로, 거짓이면 참으로



# 13. 불린 (Boolean)
print(True)
print(False)

print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print(not True)
print(not False)

print(2 > 1)
print(2 < 1)
print(3 >= 2)
print(3 <= 2)
print(2 == 2) # == 는 같다
print(2 != 2) # != 는 같지 않다 문자열에서도 가능

print(2 > 1 and "Hello" == "Hello")
print(not not True)
print(not not False)
print(7 == 7 or (4 < 3 and 12 > 10)) # (4 < 3 and 12 > 10)는 false, True or False = True

x = 3
print(x > 4 or not (x < 2 or x == 3)) # False?



# 14. type 함수
print(type(3)) # 정수형
print(type(3.0)) # 소수형
print(type("3")) # 문자열

print(type("True"))
print(type(True))


def hello(): # 함수를 정의했다 파이썬에서는 함수도 자료형에 속한다
    print("Hello world!")

print(type(hello)) # hello의 자료형은 함수
print(type(print)) # print의 자료형도 함수, 사용자가 직접 정의한 함수가 아닌 내장된 함수라는 뜻이다



# 15. 자료형 퀴즈
print(int(2.5) + int(3.8) > int(str(1) + str(2))) # 5 > 12 false
print((12 >= 10 and not 3 > 4) or 3 ** 2 != 9) # true
print(True and (True or False)) # true
print(not True or (True and False)) # false
print(False == False) # true