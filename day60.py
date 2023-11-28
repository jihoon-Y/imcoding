# 03. 리스트 정렬

numbers = [19, 13, 2, 5, 3, 11, 7, 17]

# 이 리스트를 작은 순으로 정렬하기 위해서는 두 가지가 필요하다

new_list = sorted(numbers)  # sorted는 리스트를 새로 정렬한다
# 새로 정렬한 걸 새로운 리스트라는 변수에 넣어준다
print(new_list)

# 만약 반대 순서로 정렬하고 싶다면 새로운 파라미터 값을 준다
new_list = sorted(numbers, reverse=True)  # 반대로 정렬하라는 뜻
print(new_list)
print(numbers)

# sorted 함수는 기존 리스트를 전혀 건드리지 않는다
# 정렬할 새로운 리스트를 만들어서 리턴할 뿐

# print(numbers.sort())  # none이 나오는 이유는 sort는 아무것도 리턴하지 않기 때문
numbers.sort()  # numbers 리스트 자체를 바꿨기 때문에 numbers를 출력해야 한다
print(numbers)

# 반대로 출력하고 싶을 때는
numbers.sort(reverse=True)
print(numbers)