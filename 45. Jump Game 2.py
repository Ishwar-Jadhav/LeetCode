nums = [2,3,1,1,4]
# Output: 2

r,es = 0
l = r = 0

while r < len(nums) - 1:
    farthest = 0
    for i in range(l, r + 1):
        farthest = max(farthest, i + nums[i])
    l = r + 1
    r = farthest
    res += 1
print(res)