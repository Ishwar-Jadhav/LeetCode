height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

res = 0
l, r = 0, len(height)-1
while l <= r:
    area = (r - l) * min(height[l], height[r])
    # print(area)
    res = max(res, area)
    # print(res)
    if height[l] < height[r]:
        l += 1
    # elif height[r] < height[l]:
    #     r -= 1
    else:
        r -= 1
print(res)
