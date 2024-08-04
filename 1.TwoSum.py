'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap = {}
        # for i, n in enumerate(nums):
        #     diff = target - n
        #     if diff in hashmap:
        #         return [hashmap[diff], i]
        #     hashmap[n] = i
        # return

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # dict1 = {}
        # for i in range (len(nums)):
        #     if target - nums[i] in dict1:
        #         return [dict1[target-nums[i]], i]
        #     else:
        #         dict1[nums[i]] = i

        # dict1 = {}
        # for i in range(len(nums)):
        #     if target-nums[i] in dict1:
        #         return [dict1[target-nums[i]], i]
        #     else:
        #         dict1[nums[i]] = i

        # print(dict1)

        # for j in range(i+1, len(nums)):
        #     if nums[i]+nums[j] == target:
        #         return [i,j]
