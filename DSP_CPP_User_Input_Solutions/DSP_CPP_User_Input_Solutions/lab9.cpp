// Problem 09: Circular convolution (matrix method)
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

    vector<vector<double>> X(N, vector<double>(N));

    // Circulant matrix: X[i][j] = x[(i-j) mod N]
    for (int i = 0; i < N; ++i)
        for (int j = 0; j < N; ++j)
            X[i][j] = x[(i - j + N) % N];

    cout << "Circulant matrix:\n";
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j)
            cout << X[i][j] << " ";
        cout << "\n";
    }

    for (int i = 0; i < N; ++i)
        for (int j = 0; j < N; ++j)
            y[i] += X[i][j] * h[j];

    cout << "Circular convolution (matrix method) = ";
    for (double v : y) cout << v << " ";
    cout << "\n";
    return 0;
}
