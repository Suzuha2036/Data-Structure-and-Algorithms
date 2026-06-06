#include <iostream>
using namespace std;


int main()

{
    int amount, one, five, ten, twenty;
    cout<<"Welcome to Coin Counter"<< endl;
    cout<<"Enter current money:";
    cin>>amount;
    
    twenty = amount / 20;
    amount -= (twenty * 20);
    ten = amount / 10;
    amount -= (ten * 10);
    five = amount / 5;
    amount -= (five * 5);
    one = amount / 1;
    amount -= (one * 1);
    
    cout<<"20:"<<twenty<< endl;
    cout<<"10:"<<ten<< endl;
    cout<<"5:"<<five<< endl;
    cout<<"1:"<<one<< endl;

    return 0;
}
