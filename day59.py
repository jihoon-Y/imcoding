# 프로그래밍과 데이터 in Python
# 04. 리스트 인덱싱 연습

# greetings 리스트의 원소를 모두 출력하는 프로그램을 작성하라
# 조건1 : while문과 리스트의 개념을 활용해야 한다
# 조건2 : 안녕 니하오 곤니찌와 올라 싸와디캅 헬로 봉주르 가 순서대로 출력되어야 한다

greetings = ["안녕", "니하오", "곤니찌와", "올라", "싸와디캅", "헬로", "봉주르"]

n = 0  # n이 아니라 i를 주로 쓴다
while n <= 6:
    print(greetings[n])
    n += 1

# 이 코드를 조금 더 일반화하고 싶으면, len 함수를 사용한다

i = 0
while i < len(greetings):  # len()으로 요소의 총 개수를 지정함으로써 직접 안 세어도 됨
    print(greetings[i])
    i += 1
