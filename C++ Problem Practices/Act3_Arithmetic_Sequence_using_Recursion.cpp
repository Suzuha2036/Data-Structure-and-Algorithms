//arithmetic series using recursion

#include <iostream>
using namespace std;

int recursion(int num){
    if(num > 0){
        return num + recursion(num - 1); // 3 + 2 + 1
    }
    else{
        return 0;
    }
}

// first iteration: sum(3), 3 > 0 so call sum(2)
// second iteration: sum(2), same process call sum(1)
// third iteration: sum(1) call sum(0)
// fourth iteration sum(0), it equals zero and doesnt met condition so return 0

int main()
{
    int result = recursion(3);
    cout<<result; // value of result is 6
    return 0;
}