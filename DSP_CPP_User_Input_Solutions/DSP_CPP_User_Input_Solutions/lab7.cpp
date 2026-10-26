// Problem 07: Deconvolution using polynomial long division
// Assumes h[0] is non-zero and the input y is a convolution result.
#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
using namespace std;

int main() {
    int ny, nh;
    cout << "Enter number of samples in convolution result y: ";
    cin >> ny;
    if (ny <= 0) { cout << "Length must be positive.\n"; return 1; }
    vector<double> y(ny);
    cout << "Enter " << ny << " samples of y: ";
    for (double &v : y) cin >> v;

    cout << "Enter number of samples in known signal h: ";
    cin >> nh;
    if (nh <= 0 || nh > ny) {
        cout << "h length must be positive and no greater than y length.\n";
        return 1;
    }
    vector<double> h(nh);
    cout << "Enter " << nh << " samples of h: ";
    for (double &v : h) cin >> v;

    if (abs(h[0]) < 1e-12) {
        cout << "Cannot divide: first sample h[0] must be non-zero.\n";
        return 1;
    }

    vector<double> work = y;
    int nx = ny - nh + 1;
    vector<double> x(nx, 0.0);

    for (int i = 0; i < nx; ++i) {
        x[i] = work[i] / h[0];
        for (int j = 0; j < nh; ++j)
            work[i + j] -= x[i] * h[j];
    }

    cout << fixed << setprecision(4);
    cout << "Recovered signal x[n] = ";
    for (double v : x) cout << v << " ";
    cout << "\nRemainder (should be near zero for exact convolution) = ";
    for (double v : work) cout << v << " ";
    cout << "\n";
    return 0;
}
