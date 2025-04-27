def sortingAlgo(arr,length):
    for loop in range(length):
        for traverse in range(length):
            if arr[traverse] > arr[traverse + 1]:
                arr[traverse], arr[traverse + 1] = arr[traverse + 1], arr[traverse]
    return arr

def binarySearch(arr,targetNum,high,low):
    while low <= high:
        mid = low + (high - low) // 2
        
        if targetNum == arr[mid]:
            return mid;
        
        if targetNum < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1
    
    
arr = [3,4,1,6,10,24,55,21,53,69,99, 100]
print(f"Unsorted Array {arr}")
targetNum = int(input("Input Element to find: "))
length = len(arr)
sortedArr = sortingAlgo(arr,length - 1)
print(f"Sorted Array: {sortedArr}")
result = binarySearch(sortedArr,targetNum, length -1 ,low = 0)

if result == -1:
    print("No element found")
else:
    print(f"Element {targetNum} found at index {result}")
