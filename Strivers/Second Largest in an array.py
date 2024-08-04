arr = [873, 54, 234, 555, 800, 800]
if len(arr) < 2:
    print(-1)
else:
    print("In else")
    arr.sort()
    largest = arr[-1]
    print("Largest = ", largest)
    for i in range(len(arr) - 1, -1, -1):
        print(arr[i])
        if arr[i] != largest:
            print("Second largest = ", arr[i])
            break
        else:
            print("not found")

print("end")        