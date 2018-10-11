#include <iostream>
using namespace std;

void initialize(double * arr, int * range, int value);
void printarray(double * arr);

int main() {
    // Define domain
    double x[100] = {0};
    printarray(x);

    // Define initial conditions
    int range[2] = {0, 10};
    initialize(x, range, 1);

    // Define simulation parameters
    const auto dx = 1e-3;
    const auto dt = 1e-4;
}

void initialize(int * arr, int range[2], int value) {
    for (int i = range[0]; i < range[1]; ++i) {
        arr[i] = value;
    }
}

void printarray(double (&arr)[]) {
    for (auto x : arr) {
        cout << x << " ";
    }
    cout << endl;
}
