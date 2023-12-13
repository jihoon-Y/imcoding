# 01. 사전
# key-value pair(키-값 쌍)

# 리스트를 쓰면 값들을 원하는 순서로 정리해 놓을 수 있다
# 그리고 이 리스트에서 값들을 받아 오려면 범위 안에 있는 정숫값으로 인덱싱 하면 된다
# 이렇게 여러 값을 정리한 자료형으로, 파이썬에는 사전이란 게 있다
my_list = [2, 3, 5, 7, 11, 13]
print(my_list[1])
print(my_list[3])

# 사전에서는 단어와 뜻이 하나의 쌍을 이룬다
# 마찬가지로 파이썬의 사전은 key와 value가 하나의 페어(쌍)을 이룬다

my_dictionary = {
    5: 25,
    2: 4,
    3: 9
}  # 키가 5, 값이 25인 쌍, 키가 2, 값이 4인 쌍, 키가 3, 값이 9인 쌍을 만든 것이다

print(type(my_dictionary))  # my_dicyionary 변수가 담고 있는 값은 사전 자료형이다

# 사전에서의 인덱싱
# 대괄호 안에 키를 넣어주면 된다
print(my_dictionary[3])

# 새로운 쌍 추가
my_dictionary[9] = 81  # 9라는 키에 값 81을 저장하고 싶다
print(my_dictionary)

# 사전과 리스트와의 차이
# 리스트는 인덱스가 순서대로 0, 1, 2, 3, 4, ... 이런 식으로 진행된다
# 사전을 만들 때에는 5, 2, 3, ... 이렇게 아무 순서로 키를 정해주었다
# 또, 사전의 키는 정수형일 필요가 없다

my_family = {
    '엄마': '방미',
    '아빠': '용성',
    '아들': '지훈',
    '딸': '예슬'
}

print(my_family['아빠'])


# 02. 영어 단어장
vocab = {
    'sanitizer': '살균제',
    'ambition': '야망',
    'conscience': '양심',
    'civilization': '문명'
}
print(vocab)


vocab['privilege'] = '특권'
vocab['principle'] = '원칙'
print(vocab)


# 03. 사전 활용법
# 사전에 어떤 값들이 있는지 그 목록이 필요할 때
print(my_family.values())

# 특정 값이 있는지 확인하고 싶을 때 (불린값)
print('라희' in my_family.values())

# 만약 이 목록으로 반복문을 돌고 싶을 때
for value in my_family.values():
    print(value)  # for문으로 리스트를 돌듯 값을 하나씩 받아올 수 있다!

# 값 대신 키 목록을 받아오고 싶을 때
print(my_family.keys())
for key in my_family.keys():
    value = my_family[key]  # 이렇게 하면 사전에 있는 값을 받아올 수 있다
    print(key, value)  # key를 새로운 value에 저장할 수도 있다
    # 그리고 key와 value를 모두 출력하면 모든 쌍을 출력할 수 있다!
# 하지만 지금은 키를 먼저 받아 오고, 그 키를 통해 값을 받아옴으로써 두 단계를 거쳤다

# 한 단계로 키와 값을 한 번에 받아오고 싶을 때
for key, value in my_family.items():  # 이러면 키와 밸류를 동시에 받을 수 있다
    # value = my_family[key]  # 이 줄은 필요가 없어진다
    print(key, value)


# 04. 사전 뒤집기
# key와 value를 뒤집어 주는 함수, reverse_dict를 사용하여 영-한, 한-영 사전을 만들자

# 언어 사전의 단어와 뜻을 서로 바꿔주는 함수
def reverse_dict(dict):
    new_dict = {}  # 새로운 사전
    
    # dict의 key와 value를 뒤집어서 new_dict에 저장
    for key, value in dict.items():
        new_dict[value] = key

    return new_dict  # 변환한 새로운 사전 리턴


# 영-한 단어장
vocab = {
    'sanitizer': '살균제',
    'ambition': '야망',
    'conscience': '양심',
    'civilization': '문명',
    'privilege': '특권',
    'principles': '원칙'
}

# 기존 단어장 출력
print("영-한 단어장\n{}\n".format(vocab))

# 변환된 단어장 출력
reversed_vocab = reverse_dict(vocab)
print("한-영 단어장\n{}".format(reversed_vocab))


# 05.투표 집계하기
# 파이썬 리스트 votes에는 투표 결과가 저장되어 있다
# 이 리스트 votes의 정보를 토대로 사전 vote_counter에 득표수를 정리하는 것이 목표이다

# 투표 결과 리스트
votes = ['김영자', '강승기', '최만수', '김영자', '강승기', '강승기', '최만수', '김영자', \
'최만수', '김영자', '최만수', '김영자', '김영자', '최만수', '최만수', '최만수', '강승기', \
'강승기', '김영자', '김영자', '최만수', '김영자', '김영자', '강승기', '김영자']

# 후보별 득표수 사전
vote_counter = {}

# 리스트 votes를 이용해서 사전 vote_counter를 정리하기
for name in votes:
    if name not in vote_counter:
        vote_counter[name] = 1
    else:
        vote_counter[name] += 1

# 후보별 득표수 출력
print(vote_counter)


# 이 문제는 for문을 이용해서 votes에 있는 후보 이름을 순서대로 name이라는 변수에 지정하고
# name을 vote_counter 사전에 반영하면 된다

# 두 가지 경우가 있다
# 해당 후보(name)가 아직 vote_counter에 없는 케이스
# 해당 후보(name)가 이미 vote_counter에 있는 케이스

# 첫 득표를 한 상황이라면 vote_counter[name] = 1 을 하면 된다
# 이미 최소 하나의 득표를 한 상황이라면 기존 득표 수에 1을 늘려주면 된다
# 즉, vote_counter[name] += 1을 하면 된다