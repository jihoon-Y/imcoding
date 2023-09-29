sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

jumin = "990120-1234567"
#index가 0부터 시작함=위치 셀 때 첫번째가 아니라 0번째부터 시작한다는 의미
print("성별 : " + jumin[7]) #필요한 값만 가져올 때 대괄호 사용
print("연 : " + jumin[0:2]) #0번째부터 2번째 직전까지,=미만 실제자리보다 +1해야됨
print("월 : " + jumin[2:4]) #2번째부터 3번째까지만 출력
print("일 : " + jumin[4:6]) #4번째부터 5번째까지만 출력

print("생년월일 : " + jumin[:6]) #처음(0번째)부터 6번째까지
print("뒤 7자리 : " + jumin[7:]) #7번째부터 끝까지
print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) #맨뒤에서 7번째부터. 맨 뒷자리는 -1번째인거임

python = "Python is Amazing"
print(python.lower()) #소문자로
print(python.upper()) #대문자로
print(python[0].isupper()) #python의 0번째문자가 대문자입니까?
print(len(python)) #python의 문장길이(공백포함)
print(python.replace("Python","java")) #문자변환

index = python.index("n") #n의 위치 찾기
print(index)
index = python.index("n", index + 1) #두번째 n찾기
print(index)

배고파="배아픈데 배고파"
print(배고파.index("배")+1)

print(python.find("n"))
print(python.find("java")) #없는 단어라 -1로 출력됨
#print(python.index("java")) #python이라는 변수에 java가 없기 때문에 오류내고 종료해버려서 그 다음 함수도 출력안됨
print("hi")
print(python.count("n")) #변수에 n이 총 몇번 등장하는지