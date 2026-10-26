
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N;

    cout << "Enter common length N: ";
    cin >> N;

    if (N <= 0) {
        cout << "N must be positive.\n";
        return 1;
    }

    vector<double> x(N), h(N), y(N, 0.0);

    cout << "Enter samples of x1: ";
    for (double &v : x)
        cin >> v;

    cout << "Enter samples of x2: ";
    for (double &v : h)
        cin >> v;

    // Circular convolution using the book's circle-method
    for (int n = 0; n < N; n++) {
        for (int k = 0; k < N; k++) {
            int index = (n - k + N) % N;
            y[n] += x[k] * h[index];
        }
    }

    cout << "\nCircular convolution result:\n";
    for (double v : y)
        cout << v << " ";

    cout << "\n";
    return 0;
}
