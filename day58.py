# 프로그래밍과 데이터 in Python
# 02. 리스트 함수

numbers = []
# 비어있는 리스트를 만들었다 여기서 몇 개의 요소가 있는지 알고 싶을 때 어떻게 할까?
# len 함수
# 리스트에 값이 몇 개 있는지 리턴
len(numbers)
print(len(numbers))

# append 함수(추가 연산)
# 리스트의 가장 오른쪽 끝에 요소 추가
numbers.append(5)
numbers.append(8)
print(numbers)
print(len(numbers))


numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# del 함수
# 삭제하고 싶은 요소를 리스트에서 지울 수 있다
del numbers[2]
print(numbers)

# insert 함수(삽입 연산)
# 추가하고 싶은 요소를 특정 위치에 추가할 수 있다
numbers.insert(4, 37) # 4번째 요소의 자리에 37을 추가
print(numbers)