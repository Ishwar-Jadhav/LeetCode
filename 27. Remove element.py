nums = [3,2,2,3]
val = 3

# Output: 5, nums = [0,1,4,0,3,_,_,_]

k = 0
for i in range(len(nums)):
    if nums[i] != val:
        nums[k] == nums[i]
        k += 1
print(k)
        