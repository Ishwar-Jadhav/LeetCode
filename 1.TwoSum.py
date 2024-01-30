'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''

hashmap = {}
for i, n in enumerate(nums):
    diff = target - n
    if diff in hashmap:
        return [hashmap[diff], i]
    hashmap[n] = i
return