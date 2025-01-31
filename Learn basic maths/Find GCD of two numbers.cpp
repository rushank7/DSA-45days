#include <iostream>
using namespace std;

int findgcd(int a, int b){

    while (a > 0 && b > 0 ){
        if (a>b){
            a = a%b;
        }
        else {
            b = b%a;
        }
    }



if(a == 0) {
        return b;
    }
    // If a is not 0,
    // return a as the GCD
    return a;
}

int main() {
    int a= 20, b = 15;
    
    // Find the GCD of n1 and n2
    int gcd = findgcd(a, b);

    cout << "GCD of " << a << " and " << b << " is: " << gcd << endl;

    return 0;
}
    