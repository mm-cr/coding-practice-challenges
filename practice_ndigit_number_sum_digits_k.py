"""
N and K integers.
Find how many N-digits numbers, which have the sum of their digits equals to a given number K
"""


def sum_digits(n: int) -> int:
    """
    Sum of the digits of a given number n
    :param n: integer
    :return: sum of its digits
    """
    summ: int = 0
    for digit in str(n):
        summ += int(digit)

    return summ


def solution(n:int, k:int) -> int:

    start: int = pow(10, (n-1))
    end: int = pow(10, (n)) - 1
    counter: int = 0
    # We'll keep a list of the numbers, just to check
    my_list: list[int] = []

    for val in range(start, end):
        if sum_digits(val) == k:
            counter += 1
            my_list.append(val)

    return counter, my_list  # type: ignore


def main():
    print(solution(2, 2))


if __name__ == "__main__":
    main()
