"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

Example 1:

Input: nums = [-2, 1,-3, 4,-1, 2, 1, -5, 4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:

Input: nums = [1]
Output: 1

Example 3:

Input: nums = [5, 4, -1, 7, 8]
Output: 23

Constraints:

    1 <= nums.length <= 105
    -104 <= nums[i] <= 104

"""

from typing import List


class Solution:
    @classmethod
    def maxSubArray(cls, nums: List[int]):
        sub_arr = nums[0]
        sub_arr_max = nums[0]
        for i in range(1, len(nums)):
            if (sub_arr < 0) or (sub_arr + nums[i] < 0):
                sub_arr = nums[i]
            else:
                sub_arr += nums[i]

            if sub_arr > sub_arr_max:
                sub_arr_max = sub_arr

        return sub_arr_max


if __name__ == '__main__':
    print(Solution.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))   # 6
    print(Solution.maxSubArray(nums=[5, 4, -1, 7, 8]))                  # 23
    print(Solution.maxSubArray(nums=[-2, -1, -4, 0, -1, 2, 3, -2, 2]))  # 5
    print(Solution.maxSubArray(nums=[-2, 1]))                           # 1
    print(Solution.maxSubArray(nums=[-2, -1]))                          # -1








