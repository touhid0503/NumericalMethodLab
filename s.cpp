#include <iostream>
using namespace std;
main() {
    int n = 5; // Number of data points
    float x[] = {1, 2, 3, 4, 5}; // Predefined values of x
    float y[] = {0.6, 2.4, 3.5, 4.8, 5.7}; // Predefined values of y
    float sumx = 0, sumy = 0, sumxy = 0, sumx2 = 0, a, b;
    for (int i = 0; i < n; i++) {
        sumx += x[i];
        sumy += y[i];
        sumxy += x[i] * y[i];
        sumx2 += x[i] * x[i];
    }
    a = (n * sumxy - sumx * sumy) / (n * sumx2 - sumx * sumx);
    b = (sumy - a * sumx) / n;
    cout << "The best fit line is: y = " << a << "x + " << b << endl;
}
