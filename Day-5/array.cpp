#include <iostream>
using namespace std;




// Looping over an array

int main() {
    int arr[5] = {10,20,30,40,50};

    for (int i = 0; i < 5; i++) {
        cout << "Value of array" << i << ":" << arr[i]<< endl;
    }
    return 0;

}