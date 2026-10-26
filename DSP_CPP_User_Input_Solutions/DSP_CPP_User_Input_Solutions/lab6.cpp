
#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

int main() {
    int N, M, zx, zh;

    cout << "Enter number of samples in x[n]: ";
    cin >> N;

    if (N <= 0) {
        cout << "Invalid sample count.\n";
        return 1;
    }

    vector<double> x(N);

    cout << "Enter samples of x[n]: ";
    for (int i = 0; i < N; i++)
        cin >> x[i];

    cout << "Enter the position of arrow in x[n] (1 to "
         << N << "): ";
    cin >> zx;

    cout << "Enter number of samples in h[n]: ";
    cin >> M;

    if (M <= 0) {
        cout << "Invalid sample count.\n";
        return 1;
    }

    vector<double> h(M);

    cout << "Enter samples of h[n]: ";
    for (int i = 0; i < M; i++)
        cin >> h[i];

    cout << "Enter the position of arrow in h[n] (1 to "
         << M << "): ";
    cin >> zh;

    if (zx < 1 || zx > N || zh < 1 || zh > M) {
        cout << "Invalid arrow position.\n";
        return 1;
    }

    // Convert 1-based arrow positions to zero-based indices
    int x0 = zx - 1;
    int h0 = zh - 1;

    int L = N + M - 1;
    vector<double> y(L, 0.0);

    // Linear convolution
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            y[i + j] += x[i] * h[j];
        }
    }

    // Output index corresponding to n = 0
    int y0 = x0 + h0;

    cout << fixed << setprecision(2);

    cout << "\n========== RESULTS ==========\n";

    cout << "x[n] = ";
    for (double v : x)
        cout << v << " ";

    cout << "\nh[n] = ";
    for (double v : h)
        cout << v << " ";

    cout << "\n\nArrow position in x[n] = " << zx;
    cout << "\nArrow position in h[n] = " << zh;

    cout << "\n\nConvolution y[n]:\n";

    for (int i = 0; i < L; i++) {
        int index = i - y0;
        cout << "y[" << index << "] = " << y[i] << "\n";
    }

    cout << "\nFinal result y[n] = ";
    for (double v : y)
        cout << v << " ";

    cout << "\n=============================\n";

    return 0;
}
