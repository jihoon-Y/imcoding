# 3-1. 연산자
print(1+1) # 2
print(3-2) # 1
print(5*2) # 10
print(6/3) # 2

print(2**3) # 2^3 = 8 **는 제곱
print(5%3) # 5를 3으로 나눈 나머지 2, %는 나머지
print(10%3) # 10을 3으로 나눈 나머지 1

print(5//3) # 5를 3으로 나눴을 때의 몫 1
print(10//3) # 10을 3으로 나눴을 때의 몫 3

print(10 > 3) # Ture 와 같은 비교 연산도 가능
print(4 >= 7) # False
print(10 < 3) # False
print(5 <= 5) # True

print(3 == 3) # True
print(4 == 2) # False
print(3 + 4 == 7) # True

print(1 != 3) # True, ==는 앞과 뒤가 같다, !=는 같지 않다
print(not(1 !=3)) # False, not은 뒤에 있는 값의 반대

print((3 > 0) and (3 < 5)) # True, and이므로 둘 다 true여야함
print((3 > 0) & (3 < 5)) # True

print((3 > 0) or (3 > 5)) # True, or이므로 둘 중 하나만 true여도 됨
print((3 > 0) | (3 > 5)) # True
print(5 > 4 > 3) # True, 연속된 연산도 가능
print(5 > 4 > 7) # False

# 3-2. 간단한 수식
print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20

number = 2 + 3 * 4 #14
print(number)
number = number + 2 #16
print(number)

number += 2 # 18, 이렇게 줄여 쓸 수도 있음
print(number)
number *= 2 # 36
print(number)
number /= 3 # 12
print(number)
number -= 10 # 2
print(number)

number %= 5 # 0
print(number)

# 3-3. 숫자처리함수
print(abs(-5)) #5, 앱솔루트=절대값
print(pow(4, 2)) # 4^2=16, 파워=제곱
print(max(5, 12)) # 12, max=최댓값
print(min(5, 12)) # 5, min=최솟값
print(round(3.14)) # 3, round=반올림
print(round(4.99)) # 5

from math import* # 지금부터 math 라이브러리의 모든 것을 이용하겠다
print(floor(4.99)) # 4, floor를 쓸 수 있어짐, floor=내림
print(ceil(3.14)) # 4, ceil=ceiling=올림
print(sqrt(16)) # 4, sqrt=square root=제곱근

# 3-4. 랜덤함수, 난수, 무작위로 수를 뽑음
from random import*

print(random()) # 0.0~1.0 미만 임의의 값 생성
print(random()*10) # 0.0~10.0 미만
print(int(random()*10)) # 0.0~10.0 미만의 정수값 생성
print(int(random()*10) + 1) # 1.0~10.0 이하의 정수값 생성
print(int(random()*45) + 1) # 1.0~45.0이하의 정수값 생성

print(randrange(1,46)) # 왼쪽 포함 오른쪽 미포함한 범위, 1부터 46 미만의 임의의 값 생성
# 미만인지 이하인지 헷갈릴 수 있다

print(randint(1,45)) # 양끝을 모두 포함한 범위
print(randint(1,45))
print(randint(1,45))
print(randint(1,45))
print(randint(1,45))
print(randint(1,45))

# 3-5. 퀴즈2
# 월 4회 스터디를 하는데, 3번은 온라인으로, 1번은 오프라인으로 진행한다.
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하라.

# 조건1 : 랜덤으로 날짜를 뽑아야 함
# 조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
# 조건3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외한다
# 조건4 : 출력문 예제 (오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.)

from random import*
day = (randint(4,28))
print("오프라인 스터디 모임 날짜는 매월" + str(day) + "일로 선정되었습니다.")

# 처음에 day = print(randint(4,28)) 로 지정해서 실행이 안 되었음
# 변수 day는 숫자라 앞에 str()로 감싸야했는데 int()로 감싸서 실행이 안 되었음




# 4-1. 문자열
sentence = '나는 지훈입니다'
print(sentence)
sentence2 = "파이썬은 재미있어요"
print(sentence2)
sentence3 = """
나는 지훈이고,
파이썬은 재미있어요"""
print(sentence3) # """ """를 사용하면 줄바꾼 문장도 출력 가능

# 4-2. 슬라이싱
jumin = "990120-1234567"
# 문자열 중에서 필요한 만큼만 잘라서 쓰는 것을 슬라이싱이라고 한다.

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # :(콜론)은 범위를 지정해주지만 random함수처럼 끝자리는 포함 안한다
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6]) # 인덱스0(첫번째자리)부터 시작한다면 0은 적지 않아도 됨
print("뒤 7자리 : " + jumin[7:]) # 끝도 마찬가지로 생략 가능
print("뒤 7자리 (뒤에부터): " + jumin[-7:]) # 뒤에서부터 위치 지정 가능

# 4-3. 문자열처리함수
python = "Python is Amazing"
print(python.lower()) # 모두 소문자로 출력
print(python.upper()) # 모두 대문자로 출력
print(python[0].isupper()) # True
print(python[0].islower()) # False [0], 첫번째 글자가 소문자인지 묻는 함수
print(len(python)) # 문자열의 길이=글자수를 출력하는 함수
print(python.replace("Python", "Java")) # 문자열에서 특정 단어를 바꾸는 함수

index = python.index("n") #index라는 변수를 지정하고, python에 어떤 문자가 어디에 위치해 있는지 출력할 수 있음
print(index) #5, 6번째 위치에 있음을 알 수 있다

index = python.index("n", index + 1) # 첫 번째 결과 다음에 또 n이 위치한 자리를 찾을 수 있다.
print(index)

# index = python.index("n", index + 2) # 두 번째 결과 다음에 또 n이 위치한 자리를 찾을 수 있다.
# print(index) 이건 왜 안되는걸까? => 없기 때문에 에러가 나는 것이라고 한다. 이건 없애기 전까지 계속 에러가 난다.

print(python.find("Java")) # 원하는 값이 문자열에 포함되지 않을 경우 -1로 출력
# 이 이후에 다른 명령문이 있어도 -1만 출력되고 계속 진행할 수 있다.

# index = python.index("n", index + 2)와 print(python.find("Java"))의 차이는 에러 유무만이 아니라 그 다음 명령문의 수행 여부도 다름

print(python.count("n")) # 문자열에서 n이 총 몇 번 나오는지 셀 수 있는 함수

# 4-3. 문자열포맷
print("a" + "b")
print("a", "b") #이 두 가지 외에도 다양한 방식이 있다.

# 방법 1
print("나는 %d살입니다." % 20) # %d를 사용하고 원하는 수치(정수만 가능)를 입력할 수 있음
print("나는 %s을 좋아해요." % "파이썬") # %s를 사용하고 원하는 문자열을 입력할 수 있음
print("Apple 은 %c로 시작해요." % "A") # %c를 사용하고 원하는 한 글자(캐릭터)를 입력할 수 있음
# %s로만 사용하면 범용성이 높다
print("나는 %s살입니다." % 20)
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간")) # 괄호에 넣으면 순서대로 입력된다

# 방법 2
print("나는 {}살입니다.".format(20)) # format 값을 중괄호에 입력하게 된다
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간")) # 순서대로 출력된다
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간")) # 중괄호 안에 숫자를 입력하면 순서 지정 가능

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20, color = "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요".format(color = "빨간", age = 20))

# 방법 4
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")
# f뒤에 문자를 쓰면, 마치 변수를 지정해서 하듯 입출력이 가능하다. 방법 3과 뭐가 다른 건지?



# 4-5. 탈출문자
print("백문이 불여일견\n백견이 불여일타") # \n=줄바꿈

# 저는 "윤지훈"입니다. 를 출력하고 싶을 때
# print("저는 "윤지훈"입니다.") 는 "ㅁ"를 하나의 문자열로 간주하여 오류가 발생한다
# 중간의 큰따옴표를 작은따옴표로 바꾸면 문제 없지만, 원하는 문자를 출력할 수는 없다
# print('저는 "윤지훈"입니다.')로 겉을 작은따옴표로 바꾸면 되지만, 통일성이 없어진다
print("저는 \"윤지훈\"입니다.") # 이때 탈출문자를 사용하면 \는 큰따옴표를 사용하겠다는 의미가 된다
print('저는 \'윤지훈\'입니다.')

# print("C:\Users\지훈>") # 경로 등을 출력할 때 \가 하나만 있으면 오류가 발생한다
print("C:\\Users\\지훈>") # \\를 입력하면 문장 내에서 \로 취급된다

print("Red Apple\rPine") # \r을 사용하면 뒷내용이 맨 앞에 덮어쓰기 된다

print("Redd\bApple") # \b는 백스페이스, 한 글자를 지우는 것이다. 근데 왜 굳이 이걸 쓰지?

print("Red\tApple") # \t는 탭, 공백을 입력한다

# 4-6. 퀴즈3

# 사이트 별로 비밀번호를 만들어 주는 프로그램을 작성하라.

# 예) http://naver.com

# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성

# 예) 생성된 비밀번호 : nav51!

site = "http://naver.com"
site2= (site[7:-4]) #규칙 1, 2는 슬라이싱
# print(site2), site2 = "naver"

site3 = (site2[:3])
# print(site3), site3 = "nav"

# print(site2.find("e")) # e가 몇번째에 위치한건지 묻는 함수라 여기선 필요 없음
# print(len(site2)) # naver의 길이 5
# print(site2.count("e")) # e의 갯수 1

print("생성된 비밀번호 : "+ str(site3) + str(len(site2)) + str(site2.count("e")) + "!")
# 함수 앞에 str 붙이는거 까먹어서 에러 떴음... 문자열 비밀번호를 출력하는 문제니까 str 입력해야 했다