// Problem 03: Multiplication of two discrete-time signals (sample by sample)
#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

int main() {
    int N;
    cout << "Enter number of samples in each signal: ";
    cin >> N;
    if (N <= 0) { cout << "N must be positive.\n"; return 1; }

    vector<double> x1(N), x2(N), y(N);
    cout << "Enter " << N << " samples of x1: ";
    for (double &v : x1) cin >> v;
    cout << "Enter " << N << " samples of x2: ";
    for (double &v : x2) cin >> v;

    for (int i = 0; i < N; ++i) y[i] = x1[i] * x2[i];

    cout << fixed << setprecision(4) << "y[n] = ";
    for (double v : y) cout << v << " ";
    cout << "\n";
    return 0;
}
