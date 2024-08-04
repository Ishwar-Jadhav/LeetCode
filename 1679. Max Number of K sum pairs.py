nums = [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]

k = 2

nums.sort()
res = 0
i = 0
j = len(nums) - 1

while i < j:
    sum = nums[i] + nums[j]
    if sum == k:
        res += 1
        i += 1
        j -= 1
    elif sum < k:
        i += 1
    else:
        j -= 1
print(res)