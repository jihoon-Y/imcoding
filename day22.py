#파일 입출력, 파이썬을 통해 파일을 열어 내용을 불러올 수도, 쓸 수도 있다.
#파일을 하나 열어서 점수정보를 써보자
score_file=open("score.txt","w", encoding="utf8")
#open으로 파일열고 괄호에 파일명, 목적(writing), utf8을 정의하지 않으면 한글이 이상하게 표기되는 경우가 있어서 웬만하면 꼭 넣어서 쓰자
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()
#score.txt라는 파일을 w(쓰기)목적으로 열었고 print내용을 파일에 쓰고 파일을 닫는 구조

score_file=open("score.txt", "a", encoding="utf8")
#append는 이어쓰기 목적
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
#print를 쓸 때는 자동줄바꿈이 됐으나 .write로 입력할 땐 줄바꿈이 없어서 따로 입력해야함
score_file.close() #실행할 때마다 입력됨


score_file=open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()

score_file=open("score.txt", "r", encoding="utf8")
print(score_file.readline()) #줄별읽기/ 한줄만 읽어오고 커서를 다음줄로 이동
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()

#프린트문 특성상 한줄씩 띄어준다. 그게 싫으면 end추가

score_file=open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()


score_file=open("score.txt", "r", encoding="utf8")
while True: #무한루프
    line=score_file.readline() #line변수만들어서 파일에서 한줄씩 불러와라
    if not line: #line이 없으면, 읽어온 내용이 없으면
        break #반복문 탈출하게 된다.
    print(line)
score_file.close()

#역시나 줄바꿈이 싫다면 print문에 end 추가하면 된다.

score_file=open("score.txt", "r", encoding="utf8")
while True:
    line=score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()


#list에 값을 다 넣어서 처리할 수도 있다.
score_file=open("score.txt", "r", encoding="utf8")
lines=score_file.readlines()
#lines라는 변수 만들고 이렇게 하면 모든 line을 가져와서 list형태로 저장한다
for line in lines:
    print(line, end="")
#score_file에 있는 모든 line을 가져와서 list형태로 넣고 list에서 한줄씩 불러와서 출력해라
score_file.close()