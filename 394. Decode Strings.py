s = "3[a]2[bc]"
# Output: "aaabcbc"

stack = []

for i in range(len(s)):
    if s[i] != "]":
      stack.append(s[i])
      print("stack = ", stack)
    else:
        print(s[i])
        substr = ""
        while stack[-1] != "[":
            substr = stack.pop() + substr
        stack.pop()
        print("substr = ", substr)

        k = ""
        while stack and stack[-1].isdigit():
            print("k = ", k)
            k = k + stack.pop()
            stack.append(int(k) * substr)

print("".join(stack))























# stack = []
# for i in range(len(s)):
#     if s[i] != "]":
#         stack.append(s[i])
#
#     else:
#         substr = ""
#         while stack[-1] != "[":
#             substr = stack.pop() + substr
#         stack.pop()
#
#         k = ""
#         while stack and stack[-1].isdigit():
#             k = stack.pop() + k
#             print(k)
#         stack.append(int(k) * substr)
# print("".join(stack))