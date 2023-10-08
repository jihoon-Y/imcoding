# 6-3. continue 와 break
# = 반복문 내에서 쓸 수 있는 기능

# 출석을 부를 때 결석한 사람이 있으면 넘어가게끔 하는 기능
absent = [2, 5, 8, 10]
no_book = [7] # 책을 안 가져옴
for student in range(1, 11): # 1부터 11미만(10)까지 있다고 설정
    if student in absent: # student라는 변수 중에 absent에 포함된 게 있다면
        continue # 계속 진행한다
    elif student in no_book:
        print("잠깐 자습하자. {0}번은 선생님이랑 얘기 좀 하자".format(student))
        break
    print("{0}번이 책을 읽어볼까?".format(student))

# continue는 계속해서 다음 반복으로 진행된다.
# break는 해당하는 조건이 충족 되었을 때, 반복문을 종료한다.



# 6-4. for
# 출석번호가 1, 2, 3, 4인데, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104가 되게끔
students = [1, 2, 3, 4, 5]
print(students)
students = [i+100 for i in students]
# 기존 students에 있는 값들을 i로 지정해서,
# 각각 100을 더한 값을 새로운 students로 지정하겠다
print(students)

# 학생 이름을 길이로 변환
students = ["jihoon", "seongyong", "moonjung"]
students = [len(i) for i in students]
# 기존 students의 변수들을 하나씩 조회하면서 각 문자열의 길이를 수치로 변환한다
# 그렇게 변환된 숫자를 새 students로 지정하는 것
print(students)

# 학생 이름을 대문자로 변환
students = ["jihoon", "seongyong", "moonjung"]
students = [i.upper() for i in students]
# 대문자 변환은 i.upper()를 사용한다
print(students)



# 6-6. 퀴즈5

# 택시기사에게 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하라

# 조건1 : 승객별 운행 소요 시간은 5~50분 사이의 난수로 정하라.
# 조건2 : 소요 시간 5~15분 사이의 승객만 매칭해야 한다.
# 조건3 : 출력문 예제
# [O] 1번째 손님 ( 소요시간 : 15분)
# [ ] 2번째 손님 ( 소요시간 : 50분)
# [O] 3번째 손님 ( 소요시간 : 5분)
# ...
# [ ] 50번째 손님 ( 소요시간 : 16분)

# 총 탑승 승객 : 2 분

# 1 : n번째 손님을 출력하는 건 while 반복문
# 2 : 소요시간은 난수를 추출하는 함수 사용한다
# 3 : 일단 총 손님 수 50명을 지정

from random import* # 랜덤함수 선언
passenger = 50 # 50명의 매치 기회
time = randrange(5,51) # 소요시간=5분~50분까지 랜덤으로 출력
while passenger >= 1: # passenger가 1이 될 때까지 반복
    if time < 16: # 소요시간이 15분 이하일 경우 매치
        print("[O] {0}번째 손님 ( 소요시간 : {1}분 )".format(passenger, time))
    else:
        print("[ ] {0}번째 손님 ( 소요시간 : {1}분 )".format(passenger, time))
    passenger -= 1

# 난수가 모두 동일하게 입력되는 문제점 발생..;;
# 그리고 승객수를 1번째에서 시작해서 50번째에서 끝내는 방법을 모르겠다

from random import *
passenger = 0 # 총 탑승 승객 수
for i in range(1, 51): # for을 썻네.. 1부터 50까지로 지정하는 방법(n번째 승객)
    time = randrange(5, 51) # 5부터 50까지로 지정하는 방법(소요시간)
    if 5 <= time <= 15: # 5분~15분 사이의 손님
        print("[O] {0}번째 손님 ( 소요시간 : {1}분)".format(i, time)) # passenger가 아니라 i로 지정해야됐다
        passenger += 1 # 탑승 승객 수 증가 처리
    else:
        print("[ ] {0}번째 손님 ( 소요시간 : {1}분)".format(i, time))
        # 매칭 실패했기 때문에 승객수에 +=1 안한다
    
print("총 탑승 승객 : {0} 분".format(passenger))