#include <iostream>
using namespace std;

void pattern7 (int N){
    for (int i = 0; i<N ;i++)
    {
        for (int j = N ;j > i; j--)
    {
                cout << " ";
            }
            cout << endl;
        }}

int main(){
    pattern7(6);
    return 0;
}