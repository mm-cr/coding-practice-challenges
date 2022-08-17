"""
In an even word, each letter occurs an even number of times.
Write a function that given a string S consisting of N characters, returns the minimum number of letters that
must be deleted to obtain an even word.

examples
1. Given S = "acbcbba", the funcition should return 1 (one letter b must be deleted)
2. Given S = "axxaxa", your function should return 2 (one letter a and one letter x must be deleted)
3. Given S = "aaaa", your function should return 0 (there is no need to delete any letters)

Write an efficient algorithm for the following assumptions:
N is an integer within the range [0...200,000]
string S consists only of lowercase letters (a-z)
"""


from collections import Counter


def solution(S):
    minimum: int = 0
    if S != "":
        count = Counter(S)
        for key, value in count.items():
            if value % 2 != 0:
                minimum += 1

    return minimum


def main():
    print(solution("abcd"))


if __name__ == "__main__":
    main()
