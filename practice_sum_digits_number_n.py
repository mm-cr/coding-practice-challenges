"""
Sum of the digits of a given number n.
"""


def solution(n: int) -> int:
    """
    Sum of the digits of a given number n
    :param n: integer
    :return: sum of its digits
    """
    summ: int = 0
    while n >= 1:
        summ = summ + n % 10  # Using n % 10 we get the first right digit of n, and we add it to sum
        n = n // 10  # Then, we strip n of that first right digit with n//10

    return summ


def solution_improved(n: int) -> int:
    """
    Sum of the digits of a given number n, BUT processing the n as a str
        (for better time complexity)
    :param n: integer
    :return: sum of its digits
    """
    summ: int = 0
    for digit in str(n):
        summ += int(digit)

    return summ


def main():
    print(solution_improved(123456))


if __name__ == "__main__":
    main()
