
#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
using namespace std;

int main() {
    int ny, nh, zy, zh;

    cout << "Enter number of samples in y: ";
    cin >> ny;

    if (ny <= 0) {
        cout << "Length must be positive.\n";
        return 1;
    }

    vector<double> y(ny);

    cout << "Enter " << ny << " samples of y: ";
    for (double &v : y)
        cin >> v;

    cout << "Enter arrow position in y (1 to " << ny << "): ";
    cin >> zy;

    cout << "Enter number of samples in h: ";
    cin >> nh;

    if (nh <= 0 || nh > ny) {
        cout << "h length must be positive and no greater than y length.\n";
        return 1;
    }

    vector<double> h(nh);

    cout << "Enter " << nh << " samples of h: ";
    for (double &v : h)
        cin >> v;

    cout << "Enter arrow position in h (1 to " << nh << "): ";
    cin >> zh;

    if (zy < 1 || zy > ny || zh < 1 || zh > nh) {
        cout << "Invalid arrow position.\n";
        return 1;
    }

    int y0 = zy - 1;
    int h0 = zh - 1;

    if (abs(h[h0]) < 1e-12) {
        cout << "Cannot divide: h[n] at the arrow must be non-zero.\n";
        return 1;
    }

    // Shift h so that its arrow sample becomes h[0]
    vector<double> hs(nh);
    for (int i = 0; i < nh; i++)
        hs[i] = h[i];

    // Deconvolution using polynomial long division
    vector<double> work = y;
    int nx = ny - nh + 1;
    vector<double> x(nx, 0.0);

    if (abs(hs[0]) < 1e-12) {
        cout << "This implementation requires the first h sample "
             << "to be non-zero.\n";
        cout << "Place the arrow at the first sample of h for this method.\n";
        return 1;
    }

    for (int i = 0; i < nx; i++) {
        x[i] = work[i] / hs[0];

        for (int j = 0; j < nh && i + j < ny; j++)
            work[i + j] -= x[i] * hs[j];
    }

    cout << fixed << setprecision(4);

    cout << "\n========== RESULTS ==========\n";

    cout << "Input y[n] = ";
    for (double v : y)
        cout << v << " ";

    cout << "\nInput h[n] = ";
    for (double v : h)
        cout << v << " ";

    cout << "\nArrow position in y = " << zy;
    cout << "\nArrow position in h = " << zh;

    cout << "\nRecovered x samples = ";
    for (double v : x)
        cout << v << " ";

    cout << "\nRemainder = ";
    for (double v : work)
        cout << v << " ";

    cout << "\n=============================\n";

    return 0;
}
