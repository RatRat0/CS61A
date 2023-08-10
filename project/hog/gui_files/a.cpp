#include <iostream>
using namespace std;

int f(int x, int y) {
    return x + y;
}

int zg(int x, int y, int zas) {
    return x + y + zas(x, y);
}

int main() {
    int x = 3, y = 6, z = 7;
    int res = f(x, y);
    int ls = g(x, y, z, a);

}
