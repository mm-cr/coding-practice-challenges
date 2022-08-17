"""
Alexa is given n piles of equal or unequal heights. In one step, Alexa can remove any number of boxes from the pile
which has the maximum height and try to make it equal to the one which is just lower than the maximum height of the
stack. Determine the minimum number of steps required to make all of the piles equal in height.

Example 1:

Input: piles = [5, 2, 1]
Output: 3
Explanation:
Step 1: reducing 5 -> 2 [2, 2, 1]
Step 2: reducing 2 -> 1 [2, 1, 1]
Step 3: reducing 2 -> 1 [1, 1, 1]
So final number of steps required is 3.
"""


def solution(A):
    A.sort(reverse=True)
    counter: int = 0

    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[j] < A[i]:
                A[i] -= A[i] - A[j]
                counter += 1

    return counter


def main():
    print(solution([1, 1, 2, 2, 2, 3, 3, 3, 4, 4]))


if __name__ == "__main__":
    main()
