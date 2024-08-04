nums = [3,1,-2,-5,2,-4]
# Output: [3,-2,1,-5,2,-4]

n = len(nums)
ans = [0] * n
print(ans)
posIndex, negIndex = 0, 1

for i in range(len(nums)):
    if nums[i] < 0:
        ans[negIndex] = nums[i]
        negIndex += 2
    else:
        ans[posIndex] = nums[i]
        posIndex += 2
print(ans)     