#selection sort
#look for the lowest value and move it to front 
#time complexity: O(n^2)

def selectionSort(num):
    arrLength = len(num)
    
    for loop in range(arrLength -1): # looping through array multiple times
        lowestIndex = loop           # getting the first element

        for iteration in range(loop + 1, arrLength): # adding +1 to every loop, so it doesnt go back to arr[0]
           # starts from loop + 1 to avoid re-checking sorted elements.
           
            if(num[lowestIndex] > num[iteration]):   # comparing lowest element to current iteration
                lowestIndex = iteration              # assigning the current iteration to lowest index
                
        num[loop], num[lowestIndex] = num[lowestIndex], num[loop] # tuple unpacking assignment / multiple assignment / swapping
         # swap the found smallest element with the element at the current loop index.
        
    print(num)
    
num = [64, 34, 25, 12, 22, 11, 90, 12, 5]
selectionSort(num)