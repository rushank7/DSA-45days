#include <iostream>
using namespace std;

void pattern5 (int N){
    for (int i = 1; i<N ;i++)
    {
        for (int j = N ;j > i; j--)
    {
                cout << "*" <<" ";
            }
            cout << endl;
        }}

int main(){
    pattern5(6);
    return 0;
}