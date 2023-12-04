# 02.range 함수
# 간편하고 깔끔함
# 메모리를 효율적으로 사용함

# 파라미터 2개 버전
# for i in range(start, stop):
#     print(i)
#     -> start부터 stop-1 까지의 범위
for i in range(3,11):  # 3부터 10까지
    print(i)


# 파라미터 1개 버전
# for i in range(stop):
#     print(i)
#     -> 0부터 stop-1까지의 범위
for i in range(10):  # 0부터 9까지
    print(i)


# 파라미터 3개 버전
# for i in range(start, stop, step):
#     print(i)
#     -> start부터 stop-1까지의 범위, 간격 step
for i in range(3, 17, 3):
    print(i)