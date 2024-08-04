nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2

l, r = 0, 0

for r in range(len(nums)):
    if nums[r] == 0:
        k -= 1
    if k < 0:
        if nums[l] == 0:
            k += 1
        l += 1
print(r - l + 1)