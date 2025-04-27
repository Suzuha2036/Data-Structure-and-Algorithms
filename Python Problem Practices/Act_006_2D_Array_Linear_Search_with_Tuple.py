# Linear Search 
# traversing and returning first target found
# time complexity = O(n)

def linearSearch(arr, target):
    for i in range(2):
        for j in range(4):
            if target == arr[i][j]:
                return i, j             #tuple
    return None                         # Return None

arr = [[1, 2, 3, 4], [3, 4, 5, 0]]
target = 12

result = linearSearch(arr, target)
if result:
    i, j = result       #unpacking the tuple into individual variables
    print(f"Array found at row {i} and column {j}")
else:
    print("Target not found in array")
