# print("Python", "Java")
# print("Python" + "Java")

# print("Python", "Java", "JavaScript", sep=" vs ")

# print("Python", "Java", sep=",", end="?") #이 문장의 끝을 줄바꿈에서 ?로 바꿔달라
# print("무엇이 더 재밌을까요?")

# import sys
# print("Python", "Java", file=sys.stdout) #표준출력
# print("Python", "Java", file=sys.stderr) #표준에러
#로그처리를 할 때, 표준출력 부분은 잘 출력되므로 신경안써도 되지만 에러같은 경우는 로그를 확인해서 프로그램을 수정해야한다.
#그럴 때는 stderr, 표준에러로 처리되는 부분에 대해서 따로 로깅을 한다던지 해서 우리가 필요하면 따로 err처리 해줄 수 있는 것이다.


#시험성적
scores = {"수학":0, "영어":50,"코딩":100} #딕셔너리이므로 키와 밸류로 들어감
for subject, score in scores.items(): #items를 쓰면 키(subject)와 밸류(score), 페어로 나옴. 쌍으로 튜플로 보내준다.
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")
    #총 8칸을 확보한 상태에서 왼쪽으로 정렬해달라는 명령
    #총 4칸을 확보한 상태에서 오른쪽으로 정렬해달라는 명령

#은행 대기순번표
# 001, 002, 003, ...

for num in range(1, 21):
    print("대기번호 : "+str(num).zfill(3))
    #총 3칸을 확보한 상태에서 값이 없는 공간에 0으로 채워달라는 명령


answer=input("아무 값이나 입력하세요 : ") #사용자 입력을 통해 값을 받을 때는 항상 문자열 형태로 입력
answer=10
#이러고 실행하면 문장 출력 후 사용자 입력 대기, 입력 후 엔터치면 answer에 문자열로 입력
print(type(answer))
print("입력하신 값은 "+ answer + "입니다.")