#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
using namespace std;

struct point {
    double x;
    double y;
};

double length(point p1, point p2);
double area_triangle(point p1, point p2, point p3);
double area_polygon(vector<point> points);

int main() {
    point point_bank[] = {{0.0, 0.0}, {2.0, 0.0}, {3.0, 1.0}, {3.0, 2.0}, {1.0, 2.0}};  // area: 4.5 units^2
    vector<point> points;
    for (point p : point_bank) {
        points.push_back(p);
    }
    cout << "Vector method: " << area_polygon(points) << endl;

    return 0;
}

double length(point p1, point p2) {
    return sqrt(pow(p2.x - p1.x, 2) + pow(p2.y - p1.y, 2));
}

double area_triangle(point p1, point p2, point p3) {
    double a = length(p1, p2);
    double b = length(p1, p3);
    double c = length(p2, p3);
    double s = (a + b + c)/2;
    return sqrt(s * (s - a) * (s - b) * (s - c));
}

double area_polygon(vector<point> points) {
    point base_point = points.back();
    points.pop_back();
    double area = 0;
    for (short unsigned int i = 0; i + 1 < points.size(); ++i) {
        area += area_triangle(base_point, points[i], points[i + 1]);
    }
    return area;
}
