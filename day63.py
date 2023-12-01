# 07. 리스트 함수 활용하기
# 리스트 함수를 활용하여 아래의 지시 사항을 따르세요.

# numbers라는 빈 리스트를 만들고 리스트를 출력한다.
# append를 이용해서 numbers에 1, 7, 3, 6, 5, 2, 13, 14를 순서대로 추가한다 그 후 리스트를 출력한다
# numbers 리스트의 원소들 중 홀수는 모두 제거한다. 그 후 다시 리스트를 출력한다
# numbers 리스트의 인덱스 0 자리에 20이라는 수를 삽입한 후 출력한다
# numbers 리스트를 정렬한 후 출력한다

# 빈 리스트 만들기
numbers = []
print(numbers)

# numbers에 값들 추가
numbers.append(1)
numbers.append(7)
numbers.append(3)
numbers.append(6)
numbers.append(5)
numbers.append(2)
numbers.append(13)
numbers.append(14)
print(numbers)

# numbers에서 홀수 제거
i = 0
while i < len(numbers):
    if numbers[i] % 2 == 1:
        del numbers[i]
    else:
        i += 1
print(numbers)

# numbers의 인덱스 0 자리에 20이라는 값 삽입
numbers.insert(0, 20)
print(numbers)

# numbers를 정렬해서 출력
numbers.sort()
print(numbers)
