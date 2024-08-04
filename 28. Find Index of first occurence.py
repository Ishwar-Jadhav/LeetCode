haystack = "sadbutsad"
needle = "sad"
# Output: 0

if needle == " ":
    print(0)

for i in range(len(haystack) + 1 - len(needle)):
    if haystack[i: i + len(needle)] == needle:
        print(i)
print(-1)