"""
You are given a string s consisting only of lowercase English letters.
In one move, you can select any two adjacent characters of s and swap them.
Return the minimum number of moves needed to make s a palindrome.
Note that the input will be generated such that s can always be converted to a palindrome.

Example 1:

Input: s = "aabb"
Output: 2
Explanation:
We can obtain two palindromes from s, "abba" and "baab".
- We can obtain "abba" from s in 2 moves: "aabb" -> "abab" -> "abba".
- We can obtain "baab" from s in 2 moves: "aabb" -> "abab" -> "baab".
Thus, the minimum number of moves needed to make s a palindrome is 2.

Example 2:

Input: s = "letelt"
Output: 2
Explanation:
One of the palindromes we can obtain from s in 2 moves is "lettel".
One of the ways we can obtain it is "letelt" -> "letetl" -> "lettel".
Other palindromes such as "tleelt" can also be obtained in 2 moves.
It can be shown that it is not possible to obtain a palindrome in less than 2 moves.

Constraints:

    1 <= s.length <= 2000
    s consists only of lowercase English letters.
    s can be converted to a palindrome using a finite number of moves.
"""


def solution(S):
    word: list[str] = list(S)
    count: int = 0
    left_index: int = 0
    right_index: int = len(word)-1
    num_checks: int = len(word)//2

    while num_checks >= 1:
        if word[left_index] != word[right_index]:
            index: int = right_index - 1
            while index > left_index and word[left_index] != word[index]:
                index += -1

            if index == left_index:
                word[left_index], word[left_index+1] = word[left_index+1], word[left_index]
                count += 1
            else:
                while index < right_index:
                    word[index], word[index+1] = word[index+1], word[index]
                    count += 1
                    index += 1

                left_index += 1
                right_index -= 1

        else:
            left_index += 1
            right_index -= 1

        num_checks -= 1

    return count


def main():
    print(solution("letelt"))


if __name__ == "__main__":
    main()
