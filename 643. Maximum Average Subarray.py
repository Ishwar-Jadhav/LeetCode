nums =[1, 12, -5, -6, 50, 3]
k = 4

currSum = maxSum = sum(nums[:k])
print(currSum)

for i in range(k, len(nums)):
    print(nums[i-k])
    currSum = currSum + nums[i] - nums[i - k]
    print(currSum)
    maxSum = max(currSum, maxSum)
print("Result = ", maxSum/k)


# sums = []
# for i in range(len(nums)-3):
#     sum = nums[i] + nums[i+1] + nums[i+2] + nums[i+3]
#     sums.append(sum)
#     print(sums)
#     i += 1
# res = max(sums) / k
# print(res)