#include<iostream>
#include <vector>
#include <algorithm>
using namespace std;

int countdigits(int n){

    int cnt = 0;

    while(n>0) {
        cnt = cnt +1;
        n = n/10;
    }
    return cnt;
}

int main(){
    int N = 412412;
    cout << "N: " << N << endl;
    int digits = countdigits(N);
    cout << "Number of digits in N: " << digits << endl;
    return 0;
}