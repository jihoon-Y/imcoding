# 제어문13. 피보나치 수열(Fibonacci Sequence)

# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 , ... 

# 우선 피보나치 수열의 1번 항과 2번 항은 각각 1이다
# 3번 항부터는 바로 앞 두 항의 합으로 계산된다
# 예를 들어서 3번 항은 1번 항(1)과 2번 항(1)을 더한 2이며,
# 4번 항은 2번 항(1)과 3번 항(2)을 더한 3이다

# 피보나치 수열의 첫 50개 항을 차례대로 출력하는 코드를 작성하라

previous = 0
current = 1
i = 1

while i <= 50:
    print(current)
    temp = previous  # previous를 임시 보관소 temp에 저장
    previous = current
    current = current + temp  # temp에는 기존 previous 값이 저장돼 있음
    i += 1
