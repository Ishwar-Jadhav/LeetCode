from collections import Counter
s = "leetcode"
#Output: 0

hashmap = Counter(s)
print(hashmap)

for index in range(len(s)):
    if hashmap[s[index]] == 1:
        print(index)

print(-1)
