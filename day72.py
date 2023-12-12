# 07.리스트 뒤집기

# 리스트 내 요소들의 순서를 거꾸로 뒤집으려고 한다

# [1, 4, 7]이 있으면 1과 7의 위치를 바꾸어서 [7, 4, 1]로 만든다
# [1, 4, 7, 11]이 있으면 1과 11의 위치를 바꾸고, 4와 7의 위치를 바꾸어서 [11, 7, 4, 1]로 만든다
# 아래와 같이 numbers라는 리스트가 주어졌을 때, for문을 사용하여 리스트를 거꾸로 뒤집어 보자

numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# 리스트 뒤집기
for left in range(len(numbers) // 2):
    # 인덱스 left와 대칭인 인덱스 right 계산
    right = len(numbers) - left - 1

    # 위치 바꾸기
    temp = numbers[left]
    numbers[left] = numbers[right]
    numbers[right] = temp

print("뒤집어진 리스트: " + str(numbers))
