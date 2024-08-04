s = "  hello world  "
lis = s.split(" ")
print(lis)
lis.reverse()
print(lis)
for x in range(len(lis)):
    if "" in lis:
        lis.remove("")
        print(lis)
res = " ".join(lis)
print(res)



