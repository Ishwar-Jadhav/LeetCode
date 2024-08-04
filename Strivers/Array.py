arr = [3, 2, 1, 5, 2]
print(arr)
max(arr)
max = 0

for i in range(len(arr)):
    if arr[i] > max:
        max = arr[i] 
print(max)

arr1 = arr
arr1.sort()
print("Sorted max = ", arr1[-1])