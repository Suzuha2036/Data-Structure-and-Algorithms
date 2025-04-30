//doing binary search
//integer division happens in 7/2 = resulting in 3 than 3.5

#include <iostream>
using namespace std;

int binarySearch(int arr[], int target, int low, int high){
    while(low <= high){                     //              EXAMPLE USING FIRST ITERATION
    int mid = low + (high - low) / 2;       // get the middle index (3)
    
    if(target == arr[mid]){                 // compare target value to value of middle array (10 == 6): false
        return mid;
    }
    if(target < arr[mid]){                  // if array value is greater than target value (10 < 6) : false
        high = mid - 1;                     
    }
    else{                                   // target value = 10 > arr[3] value = 6
        low = mid + 1;                      // low = 4 (3 + 1)
    }
    //  second ITERATION
    // low = 4, high 7
    // 4 <= 7: true
    // mid = 4 + ( 7 - 4 ) / 2 = 5 (in integer mode calculator)
    // arr[5] = 8 < target = 10: true then move right
    // low = 5 + 1 = 6
    
    //  third ITERATION
    // low = 6, high = 7
    // 6 <= 7: true
    // mid = 6 + (7 - 6) / 2 = 6
    // arr[6] value is 10, so the condition target == arr[mid] is also true
    // then it returns the mid value which is 6
    
    
} // iterate until condition turns false
    return -1;      //use return -1 if there is no index found
}


int main()
{
    int arr[] = {2,3,5,6,7,8,10,11};
    int target = 10;
    int low = 0;
    int high = sizeof(arr) / sizeof(arr[0]); // get the size of array
    
    int result = binarySearch(arr, target, low, high - 1); // high - 1, get the indexes of every elements
    
    if(result == -1){
        cout<<"No index found";
    }
    else{
        printf("Element %d found at index %d", target, result); //target found at index 6
    }

    return 0;
}
