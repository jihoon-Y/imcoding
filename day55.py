# 제어문14. 구구단만들기

# while문을 사용해서 구구단을 출력하는 코드를 작성하라

# 이 문제는 '중첩 while문'이라는 개념을 사용해야 한다
# 중첩 while문은 while문의 동작 부분 안에 또 다른 while문을 넣는 것을 뜻한다

i = 1
while i <= 9:
    j = 1
    while j <= 9:
        print("{} * {} = {}".format(i, j, i * j))
        j += 1
    i += 1
