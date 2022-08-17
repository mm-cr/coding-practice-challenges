"""
In one step, any element of a given array can be either increased or decreased by 1.
Write a function that, given an array A of N integers, returns the minimum number of steps required
to make all elements equal.

Examples:

Given A = [3, 2, 1, 1, 2, 3, 1], the function should return 5. All 1s can be increased by 1 and
all 3s can be decreased by 1.

Given A = [4, 1, 4, 1], the function should return 6. All 4s can be decrease by 1 three times.

Write an efficient algorithm for the following assumptions:

- N is an integer within the range [1...100,000]
- each element of array A is an integer within the range [1...4]
"""


def solution(A):
    len_A: int = len(A)
    index_target_value: int = 0
    target_value: int = 0
    min_steps: int = 0

    # sort the array in ascending order
    A.sort()

    # set the target value for the index, according if the length of the array is odd or even
    if len_A % 2 != 0:
        index_target_value = len_A//2
    else:
        index_target_value = (len_A//2)-1

    # set the target value, we'll set all elements of the array to this value
    target_value = A[index_target_value]

    # process the array
    for index in range(len_A):
        if A[index] < target_value:
            min_steps += (target_value - A[index])
        elif A[index] > target_value:
            min_steps += (A[index] - target_value)

    return min_steps


def main():
    print(solution([3, 3, 3]))


if __name__ == "__main__":
    main()
