arr = [1,2,2,1,1,3]
#OP : True

dict = {}
# checking occurences
print(dict)
for i in arr:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
# now checking unique
setx = set(dict.values())
print(dict, setx)
if len(dict) == len(setx):
    print("True")
else:
    print("False")