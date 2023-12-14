# 4.파이썬 데이터의 비밀
# 01.aliasing

x = 5
y = x
y = 3
print(x)  # 5가 나온다
print(y)  # 3이 나온다

# 파이썬에서 어떤 값을 변수에 저장하는 것은 그 값에 '이름표'를 주는 것과 같다
# 한 이름표는 한 곳에만 달릴 수 있다

x = [2, 3, 5, 7, 11]
y = x
y[2] = 4
print(x)
print(y)

# 여기서는 이름표를 아직 같이 사용하고 있기 때문에 동일한 리스트가 출력된다
# 이때 y는 x의 가명(alias)이라고 부른다
# x와 y는 이름은 다르지만 같은 값을 가진다는 뜻이다

# x의 값은 유지한 채로 y의 값만 바꾸고 싶은 경우
x = [2, 3, 5, 7, 11]
y = list(x)  # list()는 리스트를 복사해주는 기능, 이때 이름표가 분리된다
y[2] = 4
print(x)
print(y)


# 02.aliasing 퀴즈

# 퀴즈1. 출력되는 내용을 골라라

x = [2, 3, 5, 7, 9]
y = x

y[2] = 11
x[4] = 13

print(y)


# 퀴즈2. 출력되는 내용을 골라라

x = ["이가훈", "김민주", "최고은", "우설희", "최규호"]
y = list(x)

y[0] = "강귀윤"
x[1] = "김원일"

print(x)


# 퀴즈3. 출력되는 내용을 골라라

x = ["이가훈", "김민주", "최고은", "우설희", "최규호"]
y = list(x)
z = x

y[0] = "강귀윤"
x[1] = "김원일"
z[2] = "성재훈"

print(x)


# 03.리스트와 문자열
# 리스트는 문자열과 유사한 구조를 지니고 있다
# 리스트는 어떤 자료형을 나열한 거라면 문자열은 문자를 나열한 것이다

# 인덱싱
alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

print(alphabet_list[0])
print(alphabet_list[1])
print(alphabet_list[4])
print(alphabet_list[-1])

# 리스트 인덱싱 하던 것처럼 문자열도 인덱싱이 가능하다

alphabet_string = 'ABCDEFGHIJ'

print(alphabet_string[0])
print(alphabet_string[1])
print(alphabet_string[4])
print(alphabet_string[-1])


# 슬라이싱
alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

print(alphabet_list[0:5])
print(alphabet_list[4:])
print(alphabet_list[:4])

# 리스트 슬라이싱처럼 문자열도 역시 가능하다

alphabet_string = 'ABCDEFGHIJ'

print(alphabet_string[0:5])
print(alphabet_string[4:])
print(alphabet_string[:4])


# 연결
str_1 = 'Hello'
str_2 = 'World'
str_3 = str_1 + str_2
print(str_3)

list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]
list_3 = list_1 + list_2
print(list_3)


# 길이
my_list = [2, 3, 5, 7, 11]
print(len(my_list))

my_string = 'Hello World!'
print(len(my_string))



# 문자열과 리스트의 차이

numbers = [1, 2, 3, 4]
numbers[0] = 5
print(numbers)

# name = 'codeit'
# name[0] = 'C'
# print(name)
# 실행하면 오류가 나는데, 문자열은 리스트와 달리 수정이 불가능하기 때문이다

name = 'codeit' + 'it'
print(name)

# 수정할 수 없는데 더하는 것은 문제 없이 실행된다
# 수정한 게 아니라 이어 붙여서 새로운 문자열을 만들었을 뿐이기 때문이다



# 04.리스트와 문자열 정리

# 리스트와 문자열은 굉장히 비슷하다
# 리스트가 어떤 자료형들의 나열이라면, 문자열은 문자들의 나열이라고 할 수 있다

# 인덱싱 (Indexing)
# 두 자료형은 공통적으로 인덱싱이 가능하다

# 알파벳 리스트의 인덱싱
alphabets_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(alphabets_list[0])
print(alphabets_list[1])
print(alphabets_list[4])
print(alphabets_list[-1])

# 알파벳 문자열의 인덱싱
alphabets_string = 'ABCDEFGHIJ'
print(alphabets_string[0])
print(alphabets_string[1])
print(alphabets_string[4])
print(alphabets_string[-1])


# for 반복문
# 두 자료형은 공통적으로 인덱싱이 가능하다 따라서 for 반복문에도 활용할 수 있다
# 알파벳 리스트의 반복문
alphabets_list = ['C', 'O', 'D', 'E', 'I', 'T']
for alphabet in alphabets_list:
    print(alphabet)


# 알파벳 문자열의 반복문
alphabets_string = 'CODEIT'
for alphabet in alphabets_string:
    print(alphabet)


# 슬라이싱 (Slicing)
# 두 자료형은 공통적으로 슬라이싱이 가능하다

# 알파벳 리스트의 슬라이싱
alphabets_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(alphabets_list[0:5])
print(alphabets_list[4:])
print(alphabets_list[:4])

# 알파벳 문자열의 슬라이싱
alphabets_string = 'ABCDEFGHIJ'
print(alphabets_string[0:5])
print(alphabets_string[4:])
print(alphabets_string[:4])


# 덧셈 연산
# 두 자료형에게 모두 덧셈은 "연결"하는 연산이다

# 리스트의 덧셈 연산
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = list1 + list2
print(list3)

# 문자열의 덧셈 연산
string1 = '1234'
string2 = '5678'
string3 = string1 + string2
print(string3)


# len 함수
# 두 자료형은 모두 길이를 재는 len 함수를 쓸 수 있다

# 리스트의 길이 재기
print(len(['H', 'E', 'L', 'L', 'O']))

# 문자열의 길이 재기
print(len("Hello, world!"))


# Mutable (수정 가능) vs. Immutable (수정 불가능)
# 하지만 차이점이 있다
# 리스트는 데이터를 바꿀 수 있지만, 문자열은 데이터를 바꿀 수 없다는 것
# 리스트와 같이 수정 가능한 자료형을 'mutable'한 자료형이라고 부르고,
# 문자열과 같이 수정 불가능한 자료형을 'immutable'한 자료형이라고 부른다
# 숫자, 불린, 문자열은 모두 immutable한 자료형이다

# 리스트 데이터 바꾸기
numbers = [1, 2, 3, 4]
numbers[0] = 5
print(numbers)



# 05.자릿수 합 구하기

# 함수 sum_digit은 파라미터로 정수형 num을 받고, num의 각 자릿수를 더한 값을 리턴한다
# 예를 들어서 12의 각 자릿수는 1, 2이니까 sum_digit(12)는 3, 즉 1 + 2의 결괏값을 리턴한다
# 마찬가지로 486의 각 자릿수는 4, 8, 6이니까 sum_digit(486)은 18(4 + 8 + 6)을 리턴하는 것이다

# 조건1 : sum_digit 함수를 작성한다
# 조건2 : sum_digit(1)부터 sum_digit(1000)까지의 합을 구해서 출력한다


# 해설

# sum_digit 함수를 정의하기 위한 단계

# 자릿수 합을 보관하는 변수 total을 0으로 정의한다
# 정수형 num을 문자열로 바꾼다
# 문자열은 리스트와 유사하다는 점을 이용하여, 반복적으로 각 자릿수를 받는다
# 각 자릿수를 정수형으로 변환한다
# 각 자릿수를 total에 더한다
# 반복문을 이용해서 total을 모두 계산한 후, total을 리턴한다

# 자리수 합 리턴
def sum_digit(num):
    total = 0
    str_num = str(num)
    
    for digit in str_num:
        total += int(digit)

    return total


# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
digit_total = 0
for i in range(1, 1001):
    digit_total += sum_digit(i)

print(digit_total)



# 06.주민등록번호 가리기

# 주민등록번호의 마지막 네 자리 defg만 가려 주는 보안 프로그램을 만들려고 한다

# mask_security_number라는 함수를 정의하려고 하는데
# 이 함수는 파라미터로 문자열 security_number를 받고,
# security_number의 마지막 네 글자를 '*'로 대체한 새 문자열을 리턴한다

# 참고로 파라미터 security_number에는 작대기 기호(-)가 포함될 수도 있고, 포함되지 않을 수도 있는데
# 작대기 포함 여부와 상관 없이, 마지막 네 글자가 '*'로 대체되어야 한다


def mask_security_number(security_number):
    return security_number[:-4] + '****'


# 테스트
print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))



# 07.팰린드롬
# "토마토"나 "기러기"처럼 거꾸로 읽어도 똑같은 단어를 '팰린드롬(palindrome)'이라고 부른다
# 팰린드롬 여부를 확인하는 함수 is_palindrome을 작성하려고 하는데
# is_palindrome은 파라미터 word가 팰린드롬이면 True를 리턴하고 팰린드롬이 아니면 False를 리턴한다
# 예를 들어서 "racecar"과 "토마토"는 거꾸로 읽어도 똑같기 때문에 True가 출력되어야 한다
# 그리고 "hello"는 거꾸로 읽으면 "olleh"가 되기 때문에 False가 나와야 하는 것이다

def is_palindrome(word):
    for left in range(len(word) // 2):
        # 한 쌍이라도 일치하지 않으면 바로 False를 리턴하고 함수를 끝냄
        right = len(word) - left - 1
        if word[left] != word[right]:
            return False

    # for문에서 나왔다면 모든 쌍이 일치
    return True


# 테스트 코드
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))
