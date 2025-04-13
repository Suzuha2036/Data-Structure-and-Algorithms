#include <iostream>
#include <queue>
using namespace std;
int main() {
    int arr[4][8] = {
        {1,2,3,4,5,6,7,8},
        {8,7,6,5,4,3,2,1},
        {8,6,4,2,3,5,6,8},
        {8,5,4,3,5,2,1,4}
    };
    for(int rows = 0; rows < 4; rows++){
        for(int columns = 0; columns < 8; columns++){
            cout<<arr[rows][columns]<<" ";
        }
        cout<<endl;
    }
    int index;
    cout<<"Enter number range 0-7:";
    cin>>index;
    
    queue<int> elements;
    
    for(int rows = 0; rows < 4; rows++){
        for(int columns = 0; columns < 8; columns++){
            if(columns == index){
                elements.push(arr[rows][columns]);
            }
        }
        cout<<endl;
    }
    while(!elements.empty()){
        cout<<elements.front();
        elements.pop();
    }

    return 0;
}