from random import randint


def generate_numbers(n):
    numbers = []

    while len(numbers) < n:
        num = randint(1, 45)
        if num not in numbers:
            numbers.append(num)

    return numbers


# 테스트 코드
print(generate_numbers(6))
