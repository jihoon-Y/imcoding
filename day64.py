# 08. 리스트 꿀팁

# 어떤 값이 리스트에 있는지 확인하는 함수를 써보자

# value가 some_list의 요소인지 확인
def in_list(some_list, value):
    i = 0
    while i < len(some_list):
        # some_list에서 value를 찾으면 True를 리턴
        if some_list[i] == value:
            return True
        i = i + 1

    # 만약 some_list에서 value를 발견하지 못했으면 False를 리턴
    return False

# 테스트
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(in_list(primes, 7))
print(in_list(primes, 12))



# 쓰는데 아주 어렵지는 않다
# 하지만 리스트에 값의 존재를 확인하는 것은 너무 자주 있는 일이라서
# 파이썬에 이미 이 기능이 내장되어 있다 in이라는 키워드를 쓰면 된다
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(7 in primes)
print(12 in primes)


# 거꾸로 값이 없는지 확인하려면 in 앞에 not을 붙이면 된다

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(7 not in primes)
print(12 not in primes)



# 리스트 안의 리스트
# 리스트 안에는 또 다른 리스트가 있을 수 있다 이를 영어로 nested list라고 부른다

# 세 번의 시험을 보는 수업
grades = [[62, 75, 77], [78, 81, 86], [85, 91, 89]]

# 첫 번째 학생의 성적
print(grades[0])

# 세 번째 학생의 성적
print(grades[2])

# 첫 번째 학생의 첫 번째 시험 성적
print(grades[0][0])

# 세 번째 학생의 두 번째 시험 성적
print(grades[2][1])

# 첫 번째 시험의 평균
print((grades[0][0] + grades[1][0] + grades[2][0]) / 3)


# sort 메소드
# 정렬된 새로운 리스트를 리턴시켜주는 sorted 함수와 다르다
# some_list.sort()는 새로운 리스트를 생성하지 않고 some_list를 정렬된 상태로 바꿔준다

numbers = [5, 3, 7, 1]
numbers.sort()
print(numbers)


# reverse 메소드
# some_list.reverse()는 some_list의 원소들을 뒤집어진 순서로 배치한다
numbers = [5, 3, 7, 1]
numbers.reverse()
print(numbers)



# index 메소드

# some_list.index(x)는some_list에서 x의 값을 갖고 있는 원소의 인덱스를 리턴해준다

members = ["영훈", "윤수", "태호", "혜린"]
print(members.index("윤수"))
print(members.index("태호"))


# remove 메소드
# some_list.remove(x)는some_list에서 첫 번째로 x의 값을 갖고 있는 원소를 삭제해준다
fruits = ["딸기", "당근", "파인애플", "수박", "참외", "메론"]
fruits.remove("파인애플")
print(fruits)
