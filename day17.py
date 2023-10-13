# 7-7. 퀴즈6
# 표준 체중을 구하는 프로그램을 작성하시오
# 남자 : 키*키*22
# 여자 : 키*키*21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시
# 조건3 : 출력예제 > 키 175cm 남자의 표준체중은 67.38kg 입니다.

def std_weight(height, gender): # 키는 m 단위 (실수), 성별은 "남자" / "여자"
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21
    
height = 175 # cm 단위
gender = "남자"
weight = round(std_weight(height / 100, gender), 2) # 이렇게 단위 변환도 가능하다
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))
# 소수점 셋째 자리까지 출력된다 round로 줄일 수 있다.