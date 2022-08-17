'''
There are N cars, numbered from 0 to N-1. Each of them has some of the M possible optional features, numbered
from 0 to M-1, for example: voice control, keyless entry, sunroof, blind spot detection, etc.
The features of a car are described as a string of M characters, where the K-th character being '1' denotes
that the car has the K-th possible feature and '0' denotes that it does not.

Two cars are similar if their descriptions differ by at most one feature.
For example: "01101" and "01001" are similar, because they differ only by feature number 2.
On the other hand, "01101" and "11110" are not similar, because they differ in feature numbers 0, 3 and 4.

Each car from the following set is similar to "011": "011", "111", "011", "010".
Notice that cars "011" and "011" are similar as their set of features is exactly the same.

Write a function that, given an array cars consisting of N strings, returns an array of integers denoting,
for every car in cars, the number of other similar cars.

Example:

Given cars = ["100", "110", "010", "011", "100"], the answer should be [2, 3, 2, 1, 2].
Car number 0 ("100") is similar to car number 1 ("110") and also to caar number 4 ("100").
'''


def is_similar(car: str, alternative: str) -> bool:
    """
    Calculates the 'string distance' between two strings using the xor operator.
    Returning 'True' if the distance is equal to 1 (or if the two strings evaluated are equal)
    Returns 'False' in any other case.
    """
    is_similar_: bool = False
    if car == alternative:
        is_similar_ = True
    else:
        # converts the binary strings to int to apply the xor
        xor: int = int(car, 2) ^ int(alternative, 2)

        # converts the result to a binary string, slicing the '0b'
        binary_xor: str = bin(xor)[2:]

        # inserts the binary string in a list. Example: ['1','0','1']
        list_xor: list[str] = list(binary_xor)

        # using map() to perform to convert a list of strings to a list of integers. Example: [1,0,1]
        list_xor_int = list(map(int, list_xor))
        if sum(list_xor_int) == 1:
            is_similar_ = True

    return is_similar_


def solution(my_list: list[str]) -> list[int]:
    len_mylist: int = len(my_list)
    # create a list of zeros, with 'len_mylist' size
    result: list[int] = [0] * len_mylist

    # a couple of loops to compare -only one time- each item in of the list with the rest
    for i in range(0, len_mylist):
        for j in range(i + 1, len_mylist):
            if is_similar(my_list[i], my_list[j]):
                result[i] += 1
                result[j] += 1

    return result


def main():
    print(solution(["100", "110", "010", "011", "100"]))


if __name__ == "__main__":
    main()
