# 05.파일 쓰기

with open('new_file.txt', 'w') as f:
    # new_txt라는 이름의 텍스트파일 형식을 w(쓰겠다)하고 f라는 변수에 저장하겠다는 뜻
    # 이제 이 파일에 무언가를 바로 쓸 수 있다
    f.write("Hello world!\n")
    f.write("My name is Codeit.\n")

# 여기서 수정하고 실행하면 텍스트 파일을 덮어쓰게 되는데
# 새로 추가하고 싶다면 w 대신에 a(append)로 바꿔 쓰면 된다
    
with open('new_file.txt', 'a') as f:
    f.write("Hello world!\n")
    f.write("My name is Codeit.\n")