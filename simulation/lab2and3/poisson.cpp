#include <stdio.h>
#include <cmath>
#include <iomanip>
#include <iostream>

using namespace std;

int fact(int x) {
    if (x == 1 || x == 0) {
        return 1;
    }
    return x * fact(x - 1);
}

double poisson_prob(double lambda, int x) {
    return (exp(-lambda) * pow(lambda, x)) / fact(x);
}

void poisson(int lambda) {  
    double temp;           
    for (int i = 0; i < 15; i++) {
        temp = poisson_prob(lambda, i);
        cout << "x = " << i << ": " << fixed << setprecision(4) << temp << endl;
    }
}

int main() {
    int lambda = 12;    
    poisson(lambda);    
    return 0;
}