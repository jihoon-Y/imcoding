# 02. strip
# strip은 문자열 앞뒤에 있는 화이트 스페이스를 없애준다
# 텍스트파일을 출력할 때 나오는 빈줄들을 없앤다는 뜻이다

# 화이트스페이스란 " ", "\t", "\n" 이런 공백들을 얘기하는 것이다
# print문은 기본적으로 엔터를 한번 친다

print("         abc    def                     ".strip())
print("  \t     \n  abc    def\n\n\n".strip())