// Problem 05: Even and odd components of a signal
// Enter an odd number of samples representing n = -M, ..., 0, ..., M.
#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

int main() {
    int N;
    cout << "Enter an ODD number of samples (e.g. 5, 7, 9): ";
    cin >> N;
    if (N <= 0 || N % 2 == 0) {
        cout << "Please enter a positive odd number of samples.\n";
        return 1;
    }

    vector<double> x(N), xe(N), xo(N);
    cout << "Enter " << N << " samples of x[n] from n=-M to n=+M: ";
    for (double &v : x) cin >> v;

    for (int i = 0; i < N; ++i) {
        xe[i] = (x[i] + x[N - 1 - i]) / 2.0;
        xo[i] = (x[i] - x[N - 1 - i]) / 2.0;
    }

    cout << fixed << setprecision(4);
    cout << "Even component x_e[n] = ";
    for (double v : xe) cout << v << " ";
    cout << "\nOdd component x_o[n] = ";
    for (double v : xo) cout << v << " ";
    cout << "\n";
    return 0;
}
