# 7-4. 키워드값
# 키워드값을 이용한 함수 호출
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="지훈", main_lang="파이썬", age=30)
profile(main_lang="자바", age=28, name="승용") # 순서 바꿔도 문제 없음



# 7-5. 가변 인자
# 사용 언어가 늘어나거나, 없어서 ""로 처리하는 것이 불편한 상황에서 사용하는 것이 가변인자이다
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\n나이 : {1}\n".format(name, age), end=" ") # 함수가 끝날 때는 줄바꿈 않고 공백입력
#     print(lang1, lang2, lang3, lang4, lang5)

# profile("지훈", 30, "Python", "Java", "C", "C++", "C#")
# profile("승용", 28, "Kotlin", "Swift", "", "", "")

def profile(name, age, *language): # 이렇게 *가변인자 형식으로 넣으면 넣고 싶은 만큼만 넣을 수 있음
    print("이름 : {0}\n나이 : {1}\n".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("지훈", 30, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("승용", 28, "Kotlin", "Swift")