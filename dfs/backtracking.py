"""
backtracking!
"""

def subset(*nums):
    """
    https://leetcode.com/problems/subsets/description/
    pre: nums has no duplicates
    """

    result = [[]]

    def backtrack(start = 0, tmp = []):
        if start == len(nums):
            return

        for i in range(start, len(nums)):
            tmp.append(nums[i])
            result.append(tmp[:])

            backtrack(i + 1, tmp)

            tmp.pop()

    backtrack()
    return result

def permutation_sum(nums, target):
    """
    modified version of https://leetcode.com/problems/combination-sum/description/
    pre: nums has no duplicates and is sorted
    """

    result = []

    def backtrack(tmp = []):
        if sum(tmp) == target:
            result.append(tmp[:])

        if sum(tmp) >= target:
            return

        for n in nums:
            tmp.append(n)
            backtrack(tmp)
            tmp.pop()

    backtrack()
    return result

def combination_sum(nums, target):
    """
    https://leetcode.com/problems/combination-sum/description/
    pre: nums has no duplicates and is sorted
    """

    result = []

    def backtrack(start = 0, tmp = []):
        if sum(tmp) == target:
            result.append(tmp[:])

        if sum(tmp) >= target:
            return

        for i in range(start, len(nums)):
            tmp.append(nums[i])
            backtrack(i, tmp) # since nums is sorted, we only get one permutation of the subset
            tmp.pop()

    backtrack()
    return result


if __name__ == '__main__':
    print(subset(0, 1, 2, 3))
    print(permutation_sum([2, 3, 6, 7], 7))
    print(combination_sum([2, 3, 6, 7], 7))
