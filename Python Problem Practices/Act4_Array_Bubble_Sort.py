#bubble sort
#complexity O(n^2)
#bubble sort goes to every element every loop, while comparing the current and next index


def bubbleSort(num):
    arrLength = len(num)
    for i in range(arrLength - 1): # loop
        for j in range(arrLength - 1): # iterate and compare
            if(num[j] > num[j+1]):
                temp = num[j]
                num[j] = num[j+1]
                num[j+1] = temp
                # also another method is "my_array[j], my_array[j+1] = my_array[j+1], my_array[j]""
                # much efficient than using temp 
    print(num)        

num = [64, 34, 25, 12, 22, 11, 90,12, 5]
bubbleSort(num)
