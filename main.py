from collections import Counter
from math import sqrt


def is_prime(n):
    prime_ = 0
    if n > 1:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                prime_ = 1
                break
        if prime_ == 0:
            return True
        else:
            return False
    else:
        return False


def solution(A, B):
    b_occurrences = Counter(B)
    b_prime = {}
    C = []
    for element, count in b_occurrences.items():
        if is_prime(count):
            b_prime[element] = count
    print(b_prime)

    for index, element in enumerate(A):
        if b_prime.get(element) is None:
            C.append(element)

    return C


A = [2, 3, 9, 2, 5, 1, 3, 7, 10]
B = [2, 1, 3, 4, 3, 10, 6, 6, 1, 7, 10, 10, 10]
# C = [2, 9, 2, 5, 7, 10]

solve = solution(A, B)
print(solve)
