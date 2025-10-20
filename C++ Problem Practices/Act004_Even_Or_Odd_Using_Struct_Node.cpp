#include <iostream>
#include <cstdlib>  // for rand(), srand()
#include <ctime>    // for time()
using namespace std;

struct node {
    int data;
    node* next;
};

int main() {
    srand(time(0)); // seed random number generator

    node* head = nullptr;
    node* tail = nullptr;

    for (int i = 0; i < 10; i++) {
        node* newNode = new node;

        // Generate random number between 1 and 100
        int num = rand() % 100 + 1;

        // Randomly decide if it should be even or odd
        bool makeEven = rand() % 2;
        if (makeEven && num % 2 != 0) num++;       // make even
        else if (!makeEven && num % 2 == 0) num++; // make odd

        newNode->data = num;
        newNode->next = nullptr;

        if (head == nullptr)
            head = newNode;
        else
            tail->next = newNode;

        tail = newNode;
    }

    node* temp = head;
    cout<<"List of even numbers: " << endl;
    while (temp != nullptr) {
        if(temp->data % 2 == 0){
            cout << temp->data << " ";
        }
        temp = temp->next;
    }
    temp = head;
    cout << endl;
    cout<<"List of odd numbers: " << endl;
    while (temp != nullptr) {
        if(temp->data % 2 == 1){
            cout << temp->data << " ";
        }
        temp = temp->next;
    }
    cout << endl;
    

    // Cleanup memory
    temp = head;
    while (temp != nullptr) {
        node* del = temp;
        temp = temp->next;
        delete del;
    }

    return 0;
}
