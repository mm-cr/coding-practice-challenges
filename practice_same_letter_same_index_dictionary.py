"""
You are given an array S consisting of N strings. Every string is of the same length M. Your task is to find a pair of
strings in array S, such that there exists a position in which both of the strings have the same letter.
Both the index in array S and the positions in the strings are numbered from zero.

For example, given S = ["abc", "bca", "dbe"], string 0 ("abc") and string 2 ("dbe") have the same letter 'b'
in position 1. On the other hand, for strings "abc" and "bca" there does not exist a position in which they
have the same letter.

Write a function that, given a zero-indexed array S of N string, returns an array describing a pair of strings from S
which share a common letter at some index. If there is no such pair, the function should return an empty array.
If there is more than one correct answer, the function can return any of them.

The result should be represented as an array containing three integers.
The first two integers are the indexes in S of the strings belonging to the pair. The third integer is the position of
the common letter.

For S = ["abc", "bca", "dbe"], as above, the result array should be represented as [0, 2, 1]. Another correct answer
is [2, 0, 1], as the order of indexes of strings does not matter.

Examples:

Given: S = ["abc", "bca", "dbe"], your function may return [0. 2, 1] as described above.

Given: S = ["zzzz",  "ferz", "zdsr", "fgtd"], your function may return [0, 1, 3].
Both "zzzz" and "ferz" have 'z' in position 3. The function may also return [1, 3, 0], which would reflect strings
"ferz", "fgtd" and letter 'f'.

Given: A = ["gr", "sd", "rg"],your function should return []. There is no pair of strings that fulfils the criteria.

Given: A = ["bdafg", "ceagi"], your function may return [0, 1, 2].

Write an efficient algorithm for the following assumptions:

- N is an integer within the range [1..30,000]
- M is an integer within the range [1..2,000]
- each element of S consists only of lovercase English letters (a-z)
- N * M <= 30,000
"""


from collections import defaultdict
from typing import DefaultDict


def solution(S):
    # we'll use a hash table (a dictionary in Python) to process the strings
    char_indexes: DefaultDict[int, DefaultDict[int, int]] = defaultdict()
    result: list = list()

    for index in range(len(S)):
        s2: str = S[index]
        for char_index in range(len(s2)):
            c: str = s2[char_index]
            if c not in char_indexes:
                # add to char_indexes the value in the var c as a key, with value empty dictionary
                char_indexes[c]: DefaultDict[int, int] = defaultdict()
            # if I have a match, return it
            if char_index in char_indexes[c]:
                return [char_indexes[c][char_index], index, char_index]

            char_indexes[c].update({char_index: index})

    return result


def main():
    print(solution(["bdafg", "ceagi"]))


if __name__ == "__main__":
    main()
