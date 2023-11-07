#숫자열 자료형
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*6)
print(3*(3+1))
#문자열 자료형
print('풍선')
print("나비")
print("ㅋ"*9)
#문자열과 계산을 합쳐서 출력도 가능

#boolean 자료형, 참/거짓
print(5>10)
print(5<10)
print(True)
print(False)
print(not True) #not을 붙이면 뒤에 오는 것의 반대가 나옴
print(not False)
print(not (5 > 10))

#애완동물을 소개해주세요
print("우리집 강아지의 이름은 연탄이에요")
print("연탄이는 4살이며, 산책을 아주 좋아해요")
print("연탄이는 어른일까요? True")

#변수는 값을 저장하는 공간
animal = "고양이"
name = "먼지"
age = 4 #문자열은 따옴표, 나이는 숫자형이라 그냥 적음
hobby = "낮잠"
is_adult = age >=4

print("우리집 "+animal+"의 이름은 "+name+"에요")
print(name+"는 " +str(age)+"살이며, "+hobby+"을 아주 좋아해요")
print(name+ "는 어른일까요? "+str(is_adult)) #boolean형도 숫자형처럼 str()을 붙인다
print(name,"는 " ,age,"살이며, ",hobby,"을 아주 좋아해요")
#+대신 ,로 하게 되면 숫자형이나 boolean형도 str()을 사용하지 않아도 된다
#근데 ,를 쓰면 무조건 띄어쓰기가 포함된다..
#주석을 달면 실행할 때 주석 부분이 무시가 된다
#그래서 소통이나 설명이 필요할 때 주석을 남김 드래그 후 [ctrl+/]눌러도 주석

'''또 이렇게
하면 여러문장이
주석처리 된다'''

#퀴즈1
station = "인천공행"
print(station+"행 열차가 들어오고 있습니다.")