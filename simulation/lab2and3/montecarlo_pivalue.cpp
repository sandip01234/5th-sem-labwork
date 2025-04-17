#include <iostream>
#include <cstdlib>  // For rand()
#include <ctime>
#include<cmath>    // For time()
using namespace std;

double estimatePi(int points) {
    int insideCircle = 0;
    double x, y;
    
    srand(time(0));
    
    for(int i = 0; i < points; i++) {
        x = (double)rand() / RAND_MAX;
        y = (double)rand() / RAND_MAX;
        
        if(x * x + y * y <= 1) {
            insideCircle++;
        }
    }
    
    return 4.0 * insideCircle / points;
}

int main() {
    int points;
    cout << "Enter number of points to simulate: ";
    cin >> points;
    
    // Input validation
    if (points <= 0) {
        cout << "ERROR! Number of points must be positive." << endl;
        return 1;
    }
    if (points < 1000) {
        cout << "WARNING: Using fewer than 1000 points may give inaccurate results." << endl;
    }
    
    double pi = estimatePi(points);
    cout << "Estimated value of PI: " << pi << endl;
    cout << "Actual value of PI: " << 3.14159265359 << endl;
    cout << "Absolute error: " << abs(pi - 3.14159265359) << endl;
    
    return 0;
}