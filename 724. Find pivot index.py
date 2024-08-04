nums = [1, 7, 3, 6, 5, 6]
#OP = 3

total = sum(nums)
leftSum = 0
for i in range(len(nums)):
    rightSum = total - leftSum - nums[i]
    if leftSum == rightSum:
        print(i)
    leftSum += nums[i]
print(-1)





# l, r = 0, 0
# lSum , rSum = 0, 0
#
# for l in range(r):
#     for r in range(-1, l, -1):
#         lSum += nums[l]
#         print(lSum)
#         rSum += nums[r]
#         print(rSum)
#         if lSum == rSum:
#             print(l + 1)


