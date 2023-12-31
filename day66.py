# for 반복문
# 할 수 있는 일은 while 반복문과 거의 같지만, 상황에 따라 더 깔끔할 수 있다

my_list = [2, 3, 5, 7, 11]

for number in my_list:  # for문을 쓰면
    print(number)  # 이 부분이 반복적으로 실행되는 것이다
# ↑ 위에 들여쓰기 되어있는 부분이 수행 부분이다
# while 문과는 다르게 조건 부분이 없다
# 조건 부분 대신, 리스트의 0번째 요소부터 마지막까지 변수로 각각 지정되며 반복하다 끝난다
# 여기서는 직접 지적한 number라는 변수에 2, 3, 5, 7, 11이 한 번씩 들어갔다가 끝나는 것이다

# 똑같은 동작을 하는 반복문을 while문으로 썼다면
my_list = [2, 3, 5, 7, 11]

i = 0
while i <len(my_list):
    print(my_list[i])
    i += 1
# 이렇게 복잡해진다

# 그렇다고 항상 for문이 사용하기 좋은 것은 아니다
# 상황에 따라 어떤 게 더 적절할지 판단하는 능력 길러야 한다