nums1 = [1, 2, 3]
nums2 = [2, 4, 6]

answer = []

set1 = set(nums1)
set2 = set(nums2)

print(set1)
print(set2)

answer1 = set1 - set2
print(answer1)
answer2 = set2 - set1
print(answer2)

answer.append([answer1, answer2])
print(answer)
