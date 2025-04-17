#include <iostream>
#include <cstdlib>  // For rand()
#include <ctime>
#include<cmath>    // For time()
using namespace std;

// Function to integrate (x² in this case)
double f(double x) {
    return x * x;
}

double monteCarloArea(double a, double b, double maxHeight, int points) {
    int underCurve = 0;
    double x, y;
    
    srand(time(0));
    
    for(int i = 0; i < points; i++) {
        // Generate random x between a and b
        x = a + (b - a) * ((double)rand() / RAND_MAX);
        // Generate random y between 0 and maxHeight
        y = maxHeight * ((double)rand() / RAND_MAX);
        
        // If point is under the curve, count it
        if(y <= f(x)) {
            underCurve++;
        }
    }
    
    // Area = rectangle area * (points under curve / total points)
    double rectangleArea = (b - a) * maxHeight;
    return rectangleArea * underCurve / points;
}

int main() {
    int points;
    double a = 0.0;      // Lower bound
    double b = 1.0;      // Upper bound
    double maxHeight = 1.0;  // Maximum height of f(x) = x² in [0,1]
    
    cout << "Enter number of points to simulate: ";
    cin >> points;
    
    double area = monteCarloArea(a, b, maxHeight, points);
    cout << "Estimated area under x^2 from " << a << " to " << b << ": " << area << endl;
    cout << "Actual area (1/3 for x^2 from 0 to 1): " << 1.0/3.0 << endl;
    cout << "Absolute error: " << abs(area - 1.0/3.0) << endl;
    
    return 0;
}