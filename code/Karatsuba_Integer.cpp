#include <iostream>
#include <chrono>
#include <cmath>
using namespace std;
using namespace std::chrono;

// 将两个大整数分为高位和低位
pair<long long, long long> splitNumber(long long num, int n) {
    long long high = num / pow(10, n / 2);
    long long low = num % static_cast<long long>(pow(10, n / 2));
    return make_pair(high, low);
}

// 递归实现卡拉兹巴算法
long long karatsuba(long long x, long long y, int n) {
    if (n <= 1) return x * y;

    auto [x1, x0] = splitNumber(x, n);
    auto [y1, y0] = splitNumber(y, n);

    long long p1 = karatsuba(x1, y1, n / 2);
    long long p2 = karatsuba(x0, y0, n / 2);
    long long p3 = karatsuba(x1 + x0, y1 + y0, n / 2);

    return p1 * pow(10, n) + (p3 - p1 - p2) * pow(10, n / 2) + p2;
}

int main() {
    long long x = 12345678; // 更小的数字
    long long y = 87654321; // 更小的数字
    int n = to_string(max(x, y)).length();

    auto start1 = high_resolution_clock::now();
    long long result_karatsuba = karatsuba(x, y, n);
    auto end1 = high_resolution_clock::now();
    auto duration_karatsuba = duration_cast<microseconds>(end1 - start1).count();

    auto start2 = high_resolution_clock::now();
    long long result_builtin = x * y;
    auto end2 = high_resolution_clock::now();
    auto duration_builtin = duration_cast<microseconds>(end2 - start2).count();

    cout << "Karatsuba Result: " << result_karatsuba << " Time: " << duration_karatsuba << "us" << endl;
    cout << "Built-in Result: " << result_builtin << " Time: " << duration_builtin << "us" << endl;

    return 0;
}
