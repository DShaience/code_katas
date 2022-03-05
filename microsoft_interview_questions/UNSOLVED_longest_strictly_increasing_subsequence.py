"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.
A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.
For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1


Constraints:
    1 <= nums.length <= 2500
    -104 <= nums[i] <= 104

"""

from typing import List


class Solution:
    @classmethod
    def lengthOfLIS(cls, nums: List[int]):
        n = len(nums)
        if n == 1:
            return 1

        i = 1
        max_len = 0
        while i < n:
            cur_len = 1
            while (i < n) and (nums[i] - nums[i-1] > 0):
                i += 1
                cur_len += 1

            if cur_len > max_len:
                max_len = cur_len
                continue

            i += 1
        return max_len


if __name__ == '__main__':
    print(Solution.lengthOfLIS([0, 1, 0, 3, 2, 3]))   # 3











# class SubArray:
#     def __init__(self, a):
#         self.sum = a
#
#     def update_subarray(self, b):
#         self.sum += b
#
#     def renew(self, b):
#         self.sum = b
#
#
# class Solution:
#     @classmethod
#     def maxSubArray(cls, nums: List[int]):
#         n = len(nums)
#         if n == 1:
#             return nums[0]
#
#         sub_arr = SubArray(nums[0])
#         sub_arr_max = sub_arr.sum
#         for i in range(1, n):
#             if sub_arr.sum > 0:
#                 if sub_arr.sum + nums[i] > 0:
#                     sub_arr.update_subarray(nums[i])
#                 else:
#                     sub_arr = SubArray(nums[i])
#             else:
#                 sub_arr = SubArray(nums[i])
#
#             if sub_arr.sum > sub_arr_max:
#                 sub_arr_max = sub_arr.sum
#
#         return sub_arr_max