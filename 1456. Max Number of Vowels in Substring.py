s = "abciiidef"
k = 3

vowels = {'a','e', 'i', 'o', 'u'}

count = 0
for i in range(k):
    count += int(s[i] in vowels)
    answer = count

    for i in range(k, len(s)):
        count += int(s[i] in vowels)
        count -= int(s[i - k] in vowels)
        answer = max(answer, count)

    print(answer)














# l, count, res = 0, 0, 0
#
# for r in range(len(s)):
#     if s[r] in vowels:
#         count += 1
#     else:
#         count = 0
#
#     if r - l + 1 > k:
#         if s[l] in vowels:
#             count -= 1
#         else:
#             count = 0
#
#         l += 1
#     res = max(res, count)
# print(res)

