# 03.split
my_string = "1. 2. 3. 4. 5. 6"
print(my_string.split("."))

# split은 괄호 안 문자열을 기준으로 나머지 문자열을 나누는 것이다
# 지금은 파라미터로 .을 지정해서 .을 기준으로 숫자들이 나뉜 것이다

# 결과 : ['1', ' 2', ' 3', ' 4', ' 5', ' 6']
# 결과에 1을 제외한 나머지는 공백이 앞에 포함되어 있다
# 이때, strip을 사용해도 되지만 파라미터를 ". "로 해도 된다

print(my_string.split(". "))
# 결과 : ['1', '2', '3', '4', '5', '6']

full_name = "Kim, Yuna"
print(full_name.split(", "))
# 이렇게 하면 ['Kim', 'Yuna']으로 깔끔하게 되는 것을 볼 수 있다

# 이 값들을 쓰려면 name_data에 넣어주고
name_data = full_name.split(", ")
# 0번 인덱스를 last_name이라는 변수로 지정해주고
last_name = name_data[0]
# 1번 인덱스를 first_name이라는 변수에 저장해준다
first_name = name_data[1]
print(first_name, last_name)
# 결과 : Yuna Kim

print("      \n\n   2    \t 3    \n   5 7   11      \n\n")
# 이번에도 split으로 문자열을 나누고 싶은데, 이런 문장은 기준을 찾기 애매하다
# 화이트스페이스를 기준으로 나누고 싶으면 파라미터 값을 안 넘겨주면 된다
print("      \n\n   2    \t 3    \n   5 7   11      \n\n".split())
# 결과 : ['2', '3', '5', '7', '11']

# 만약 이 만들어진 리스트를 사용하고 싶다고 가정해보자
numbers = "      \n\n   2    \t 3    \n   5 7   11      \n\n".split()
print(numbers[0] + numbers[1])
# 이렇게 0번 인덱스와 1번 인덱스의 값을 더하고 싶은 상황이다
# 결과에 따르면 2와 3이 더해져서 5가 되어야 하는데, 막상 결과는 23이 나온다
# split을 이용해서 리스트를 만들었을 때, 리스트의 값들은 모두 문자열이기 때문이다
# 정수 2에 정수 3을 더하고 싶은거면 int()를 씌워서 형 변환을 해주어야 한다
print(int(numbers[0]) + int(numbers[1]))