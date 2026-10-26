// Problem 06: Linear convolution of two discrete-time signals
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int nx, nh;
    cout << "Enter number of samples in x: ";
    cin >> nx;
    if (nx <= 0) { cout << "Length must be positive.\n"; return 1; }
    vector<double> x(nx);
    cout << "Enter " << nx << " samples of x: ";
    for (double &v : x) cin >> v;

    cout << "Enter number of samples in h: ";
    cin >> nh;
    if (nh <= 0) { cout << "Length must be positive.\n"; return 1; }
    vector<double> h(nh);
    cout << "Enter " << nh << " samples of h: ";
    for (double &v : h) cin >> v;

    vector<double> y(nx + nh - 1, 0.0);
    for (int i = 0; i < nx; ++i)
        for (int j = 0; j < nh; ++j)
            y[i + j] += x[i] * h[j];

    cout << "Linear convolution y[n] = ";
    for (double v : y) cout << v << " ";
    cout << "\n";
    return 0;
}
