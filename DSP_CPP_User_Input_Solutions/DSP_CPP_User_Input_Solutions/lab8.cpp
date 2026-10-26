// Problem 08: Circular convolution (circle / circular-shifting method)
// Both signals must have the same length N.
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N;
    cout << "Enter common length N of both signals: ";
    cin >> N;
    if (N <= 0) { cout << "N must be positive.\n"; return 1; }

    vector<double> x(N), h(N), y(N, 0.0);
    cout << "Enter " << N << " samples of x: ";
    for (double &v : x) cin >> v;
    cout << "Enter " << N << " samples of h: ";
    for (double &v : h) cin >> v;

    for (int n = 0; n < N; ++n)
        for (int k = 0; k < N; ++k) {
            int index = (n - k + N) % N;
            y[n] += x[k] * h[index];
        }

    cout << "Circular convolution (circle method) = ";
    for (double v : y) cout << v << " ";
    cout << "\n";
    return 0;
}
