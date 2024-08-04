word1 = "cabbba"
word2 = "aabbss"
#OP = True
#
from collections import Counter

freq1 = Counter(word1)
print(freq1)
freq2 = Counter(word2)
print(freq2)

sFreq1 = sorted(freq1.values())
print(sFreq1)
sFreq2 = sorted(freq2.values())
print(sFreq2)

keys = freq1.keys() == freq2.keys()

if sFreq1 == sFreq2 and keys:
    print(True)
else:
    print(False)



# word1 = sorted(word1)
# print(word1)
# word2 = sorted(word2)
# print(word2)

hashmap1, hashmap2 = {}, {}

for char in range(len(word1)):
    if char in hashmap1:
        hashmap1[char] += 1
        print(hashmap1[char])
    else:
        hashmap1[char] = 1
        print(hashmap1[char])

for char in range(len(word2)):
    if char in hashmap2:
        hashmap2[char] += 1
    else:
        hashmap2[char] = 1

set1 = set(sorted(hashmap1.items()))
print(set1)
set2 = set(sorted(hashmap2.items()))
print(set2)

if set1 == set2:
    print(True)
else:
    print(False)

