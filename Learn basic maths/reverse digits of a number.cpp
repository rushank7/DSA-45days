#include <iostream>
using namespace std;

int main(){
    int n;

    cin >> n;

    int revnum = 0;

    while(n>0){
        int ls = n%10;

        revnum = (revnum*10) + ls;

        n = n/10;

    }

    cout << revnum;
}