# 제어문 07. elif문
# if문과 else문을 사용하면 프로그램이 갈 수 있는 루트는 두 가지이다
# 조건문이 true면 if문의 수행부분이, 조건문이 false면 else문의 수행부분이 실행되는 것이다

def print_grade(midterm_score, final_score):
    total = midterm_score + final_score
    if total >= 90:
        print("A")
    elif total >= 80:
        print("B")
    elif total >= 70:
        print("C")
    elif total >= 60:
        print("D")
    else:
        print("F")


# 테스트 코드
print_grade(40, 45)
print_grade(20, 35)
print_grade(30, 32)
print_grade(50, 45)