nums = [1, 2, 3, 1]
k = 3
#Op = true

window = set()
l = 0

for r in range(len(nums)):
    if r - l > k:
        window.remove(nums[r])
        l += 1
    if nums[r] in window:
        return True
    window.add(nums[r])
return False






# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if nums[i] == nums[j] and abs(i - j) == k:
#             print(nums[i], nums[j])
#             print(i, j)
#             print(True)
#         else:
#             j += 1
#     i += 1
        # if nums[i] == nums[j]:
        #     answer = abs(nums[i], nums[j])