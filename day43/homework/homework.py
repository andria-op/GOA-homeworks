# 1
def descending_order(num):
    return int(''.join(sorted(str(num), reverse=True)))
# 2
def array_diff(a, b):
    return [item for item in a if item not in b]
# 3
def spinWords(sentence):
    words = sentence.split()
    return ' '.join([word[::-1] if len(word) >= 5 else word for word in words])
# 4
def diamond(n):
    if n < 1 or n % 2 == 0:
        return None
    result = []
    for i in range(1, n + 1, 2):
        result.append(' ' * ((n - i) // 2) + '*' * i)
    for i in range(n - 2, 0, -2):
        result.append(' ' * ((n - i) // 2) + '*' * i)
    return '\n'.join(result)
# 5
def row_sum_odd_numbers(n):
    return n ** 3
# 6
def solution(number):
    return sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)
# 7
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
