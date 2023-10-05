# 5-3. 튜플
# = 리스트와는 다르게 내용을 변경, 추가할 수는 없다
# 그래서 기능적인 면에서는 한계가 있지만, 속도는 리스트보다 빠르다
# 내용이 변경되지 않는 경우에 튜플을 활용한다

menu = ("후라이드", "양념") # 절대 메뉴 변경은 없다는 가정 하
print(menu[0])
print(menu[1])

# menu.add("간장") 이런 식으로 .add하면 에러가 발생

# name = "지훈"
# age = 30
# hobby = "코딩"
# print(name, age, hobby)

name, age, hobby = "지훈", 30, "코딩"
print(name, age, hobby) # 그냥 변수 지정하는거랑 뭐가 다른거지?...



# 5-4. 집합(set)
# = 중복이 안 되고 순서가 없다

my_set = {1, 2, 3, 3, 3}
# 사전에서도 중괄호를 사용했지만 거기서는 키와 밸류로 나뉘고 여기선 그냥 값의 나열이다
print(my_set) # 중복 허용 안해서 1, 2, 3만 출력된다

python = {"지훈", "승용", "희재"}
java = set(["승용", "동해"]) # 리스트로 먼저 만들고 set으로 앞뒤로 감싸주는 형식
# 중괄호 안에 나열하는 것이 아니라 set([]) 형식으로도 정의 가능

# 교집합 (공통분모 찾기)
print(java & python)
print(java.intersection(python)) # 둘 다 교집합 추출 가능

# 합집합
print(java | python) # 둘 다 합집합 추출 가능
print(java.union(python)) # 집합의 원소로 취급해서 순서는 랜덤으로 추출된다

# 차집합
print(java - python)
print(java.difference(python))

# 집합에 추가해야 할 때
java.add("지훈")
print(java)

# 집합에서 제외해야 할 때
java.remove("동해")
print(java)



# 5-5. 자료구조의 변경
menu = {"커피", "우유", "쥬스"} # 세트로 생성했다
print(menu, type(menu)) # 자료형 뒤에 , type(변수) 하면 현재 자료구조를 알 수 있다

menu = list(menu) # 집합에서 리스트로 변경했다
print(menu, type(menu)) # 리스트인 걸 확인할 수 있음

menu = tuple(menu) # 리스트에서 튜플로 변경했다
print(menu, type(menu)) # 마찬가지로 튜플인 걸 확인 가능
# 세트일 땐 중괄호, 리스트일 땐 대괄호, 튜플일 땐 소괄호로 표기된다

menu = set(menu) # 다시 세트로 변경함
print(menu, type(menu))


# 5-6. 퀴즈4

# 파이썬 코딩 대회를 주최하는데, 참석률을 높이기 위해 댓글 이벤트를 진행하기로 했다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 된다.
# 이 추첨 프로그램을 작성하라.

# 조건1 : 댓글은 20명이 작성하였고, 아이디는 1~20이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle과 sample을 활용

# 출력 예제
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 --

# 활용 예제
from random import *
# list = [1, 2, 3, 4, 5]
# print(list)
# shuffle(list)
# print(list)
# print(sample(list, 1)) # 첫 번째 인자인 'list'에서 두 번째 인자인 '1개'를 뽑겠다

# 1. list를 1:20으로 지정한다
# 2. shuffle로 한 번 섞고
# 3. sample로 치킨 당첨자 1명을 뽑는다
# 4. 그 다음 list를 한 번 재정의 해서 뽑힌 애를 제외하고 2 진행
# 5. sample로 커피 당첨자 3명을 뽑는다
# 6. 각각 뽑은 숫자들을 지정해서 양식 안에 넣으면 될듯?

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
shuffle(list1)
id1 = sample(list1, 1)
id2 = sample(list1, 3)
print(" -- 당첨자 발표 -- \n치킨 당첨자 : "+ str(id1) +"\n커피 당첨자 : "+ str(id2) +"\n-- 축하합니다 --")
# list = [1:20] 으로 했는데 안됐다 그래서 일일히 썼는데 왜 안 됐지
# 4번 list 재정의가 힘들었다;; 리스트>집합>원소제거>리스트 과정을 거치니 에러가 뜸

list1 = range(1,20) # 이렇게 생성해도 됐다
# print(type(list1)) # range를 사용하면 타입이 list가 아닌 range라서 변환이 필요함
list1 = list(list1)
# print(type(list1)) # 리스트로 변환됨

winners = sample(list1, 4) # 처음부터 4명을 뽑고 나눠준다;
print("-- 당첨자 발표 --") # {0}과 .format()을 활용해서 지정해준다
print("치킨 당첨자 : {0}".format(winners[0])) # 문자열포맷 챕터를 활용한 방법임
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 --") # 내가 생각한 방식으로는 못 푸는 건가?