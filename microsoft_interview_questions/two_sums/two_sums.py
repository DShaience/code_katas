"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
"""

from collections import defaultdict


def twoSum(nums, target):
    num_2_ind = defaultdict(list)
    for ind, num in enumerate(nums):  # O(n)
        num_2_ind[num].append(ind)

    for num in num_2_ind.keys():  # O(n)
        second_num = target - num
        if second_num in num_2_ind.keys():  # O(1)
            if num != second_num:
                return num_2_ind[num][0], num_2_ind[second_num][0]
            elif len(num_2_ind[num]) > 1:
                return num_2_ind[num][0], num_2_ind[second_num][1]


if __name__ == '__main__':
    print(twoSum([2, 7, 11, 15], 9))
    print(twoSum([3, 2, 4], 6))
    print(twoSum([3, 3], 6))



