# 7-6. 지역변수와 전역변수
# 지역변수란 함수 내에서만 쓸 수 있는 변수, 전역변수는 함수 호출이 끝나도 프로그램 내 어디서든 부를 수 있는 변수

gun = 10 # 전체 총

def checkpoint(soldiers): # 경계근무를 하는 상황이라고 가정해보자
    gun = 20
    gun = gun - soldiers # 군인만큼 총이 빠지기 때문에 gun 새로 지정
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun)) # 전체 총이 호출된다
checkpoint(2) # 2명이 경계 근무 나가는 상황, 이 함수를 호출했을 때 지역변수가 호출된다
print("전체 총 : {0}".format(gun)) # 그래서 저 안에서 할당한 gun이 호출됨

# cannot access local variable 'gun' where it is not associated with a value라는 에러 발생
# gun이라는 변수는 할당도 안되었는데 사용되었기 때문에 발생한 에러이다

gun = 10 # 전체 총

def checkpoint(soldiers):
    global gun # 이렇게 하면 전역 변수를 사용하겠다 선언하는 것이다
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2)
print("전체 총 : {0}".format(gun))

# 이렇게 보면 전역변수를 사용하는 게 좋아보이지만 길어질수록 코드가 복잡해지기 때문에
# 함수 내에서만 쓸 변수는 지역변수로 지정해주는 것이 오히려 좋다
# 가급적 파라미터로 던져서 계산하고, 반환값을 받아 사용하는 방법을 권장한다고 한다

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun, 2)
print("전체 총 : {0}".format(gun))
# 솔직히 뭐라는지 모르겠다