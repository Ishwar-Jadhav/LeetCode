nums = [-1,0,5]
target = 9
# Output: 4
print("hi")

i = 0
low = 0
high = len(nums) - 1

while low <= high:
    mid = (low + high) // 2
    if nums[mid] == target:
        print(mid)
        break
    elif target > nums[mid]:
        low = mid + 1
    else:
        print(-1)