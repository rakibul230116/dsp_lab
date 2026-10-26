// Problem 04: Amplitude scaling of a discrete-time signal
#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

int main() {
    int N;
    double A;
    cout << "Enter number of samples: ";
    cin >> N;
    if (N <= 0) { cout << "N must be positive.\n"; return 1; }

    vector<double> x(N), y(N);
    cout << "Enter scaling factor A: ";
    cin >> A;
    cout << "Enter " << N << " samples of x: ";
    for (double &v : x) cin >> v;

    for (int i = 0; i < N; ++i) y[i] = A * x[i];

    cout << fixed << setprecision(4) << "Scaled signal y[n] = ";
    for (double v : y) cout << v << " ";
    cout << "\n";
    return 0;
}
