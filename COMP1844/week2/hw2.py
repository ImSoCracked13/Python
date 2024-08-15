# Example array
lin_arr = [2, 4, 6, 8, 10]

# Target value
target = 10

# Linear search
found = False
for i in range(len(lin_arr)):
    if lin_arr[i] == target:
        print("Element", target, "found at index", i)
        found = True
        break

if not found:
    print("Element", target, "not found")



# Example sorted array
bin_arr = [1, 3, 5, 7, 9]

# Target value
target = 1

# Binary search
low = 0
high = len(bin_arr) - 1
found = False

while low <= high:
    mid = (low + high) // 2
    
    if bin_arr[mid] == target:
        print("Element", target, "found at index", mid)
        found = True
        break
    elif bin_arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Element", target, "not found")