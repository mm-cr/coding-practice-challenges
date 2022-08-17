"""
N positive integer.
Find the smallest number whose sum of digits is also N

Input: N = 10
Output: 19
(1 + 9 = 10 = N)

Input: N = 18
Output: 99
(9 + 9 = 18 = N)
"""


def solution(n: int) -> int:
    # to get the smallest number, we need to build a number with the
    #   maximum quantity of 9 digits (except when n < 9), then:

    result: int = 0

    if n < 9:
        result = n
    else:
        # 1. how many 9's can we fit on 'n'? -> n // 9 -> 'x'
        x: int = n // 9
        # 2. and what's the remainder? -> n % 9 -> 'y' (the units needed to get 'n' after adding the nines)
        y: int = n % 9
        # 3. So to get 'n' adding the digits of a number -the smaller one-,
        #    we need to build a number with first digit 'y' followed by 'x' number of nines
        x_nines: int = pow(10, x) - 1

        result = int(str(y) + str(x_nines))

    return result


def main():
    print(solution(50))


if __name__ == "__main__":
    main()
