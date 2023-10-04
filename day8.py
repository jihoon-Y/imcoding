# 5-1. 리스트
# =순서를 가지는 객체의 집합

# 지하철 칸 별로 10명, 20명, 30명이 있다고 가정
subway1 = 10
subway2 = 20
subway3 = 30
# 이전까지는 각각 변수에 하나씩 지정을 해왔다면, 리스트는 연속적인 공간으로 묶는 것이다.
# 먼말?

subway = [10, 20, 30]
# 리스트를 사용하면 하나씩 변수를 지정할 필요가 없다?는 말인듯
print(subway)

subway = ["지훈", "문정", "소연"]
print(subway)

# 소연이는 몇 번째 칸에 타고 있는가?
print(subway.index("소연")) # .index는 위치찾는거! 0, 1, 2번째라 2가 나옴

# 승용이가 다음 정류장에서 다음 칸에 탐
subway.append("승용") # .append가 뒤에 추가하는 기능인듯
print(subway)

# 병선이를 지훈과 문정 사이에 태워보자
subway.insert(1, "병선") # 넣을 위치 지정하고 넣을 것 지정하면 됨
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼내보자
print(subway.pop()) # pop은 뒤에서부터 하나씩 꺼내는 기능
print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("지훈")
print(subway)
print(subway.count("지훈")) # 이렇게 같은 값이 몇 번 나오는지 확인 가능

num_list = [12, 83, 29, 55, 10]
num_list.sort() # 오름차순 정렬인듯
print(num_list)

num_list.reverse() # 순서 거꾸로 출력
print(num_list)

num_list.clear() # 리스트에 저장된 값들을 모두 비움, 빈 리스트가 됨
print(num_list)

mix_list = ["지훈", 77, False] # 다양한 자료형을 함께 사용 가능
print(mix_list)

# 리스트를 확장할 수도 있다
num_list = [12, 83, 29, 55, 10]
mix_list = ["지훈", 77, False]

num_list.extend(mix_list) # 베이스가 될 리스트를 앞에, 합칠 리스트를 .extend 뒤 괄호에
print(num_list)


# 5-2. 사전
# 우리가 코딩에서 사용하는 사전자료형도 단어(키)와 정의(밸류) 형태로 나온다

cabinet = {3:"지훈", 55:"승용"} # 사전일 경우 {중괄호} / 리스트일 때는 [대괄호] 였다
print(cabinet[3]) # 그러니까 3이 키, "지훈"이 밸류인 것이다
print(cabinet[55])

print(cabinet.get(3)) # cabinet.get(_) 로도 사용 가능하다, 근데 왜 두 가지를 쓰지?
# print(cabinet[100]) # 밸류가 지정되지 않은 키를 찾으면 에러가 나면서 종료된다
# print("hello") # 종료돼서 hello는 출력되지 않음

print(cabinet.get(5)) # .get()을 쓰면 밸류가 없는 키를 넣어도 종료되지 않는다
print("hello") # None이라고 출력되고 다음 명령문 hello가 출력된다
# 그래서 .get()을 쓰는 듯하다 범용성이 좋은 듯

print(cabinet.get(5, "공란")) # 키 뒤에 값을 입력해두면, 밸류가 없을 때 입력한 값 출력
print("hello")

print(3 in cabinet) # 키의 여부에 따라 True or False가 출력되는 기능

cabinet = {"C3":"지훈", "T55":"승용"}
print(cabinet["C3"])
print(cabinet["T55"])

# 새로운 키를 추가, 밸류를 업데이트 가능
print(cabinet)
cabinet["F20"] = "현규" # F20이라는 키에 "현규"라는 밸류를 부여한다
cabinet["C3"] = "성주" # 만약 C3이라는 키에 밸류가 있다면 "성주"로 업데이트 된다
print(cabinet)

# 키와 밸류를 지울 수도 있다
del cabinet["C3"]
print(cabinet)

# 사용 중인 키만 출력할 수도 있다
print(cabinet.keys())

# 사용 중인 밸류만 출력할 수도 있다.
print(cabinet.values())

# 키와 밸류 짝지어서 출력도 가능
print(cabinet.items())

# 모든 키와 밸류를 초기화하고 싶을 때
cabinet.clear()
print(cabinet) # 아무것도 없어서 {}만 출력된다