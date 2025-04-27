import numpy as np #using numpy for array

def binarySearch(target,num,high,low = 0): #default parameter value
    while low <= high:
        mid = low + ( high - low ) // 2
        if num[mid] == target:
            return mid
        elif target < num[mid]:
            high = mid - 1
        else:
            low = mid + 1
            
    return -1

num = np.array([1,2,3,4,6,7,8,10])
lengthOfNum = len(num) #getting array size
target = int(input())
result = binarySearch(target,num,lengthOfNum - 1)

print(f"found at index {result}"if result != -1 else "not found") #ternary expression
