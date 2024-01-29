'''
Given an integer array nums, return true if any value appears at least twice in thearray, and return false if every element is distinct.

Example
Input: nums = [1, 2, 3, 1]
Output: true
'''
def function(n):
    hashset = set()
    for n in nums:
        if n in hashset:
            return True
        else:
            hashset.add(n)
    return False