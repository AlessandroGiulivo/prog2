/*
SLINDING-WINDOW(S, x, y)
let A be an empty array
n <- |S|
i <- 0
while i <= n-x do
    append S[i,...,i+x] to A
    i <- i + y
return A
*/

#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<string> sliding_window(string s, int x, int y) {
    vector<string> A;
    int n = s.length();
    int i = 0;
    while (i < n - x + 1) {
        A.push_back(s.substr(i, x));
        i = i + y;
    }
    return A;
}

int main() {
    string s;
    int x;
    int y;
    cin >> s >> x >> y;
    vector<string> res = sliding_window(s, x, y);
    for (auto i = res.begin(); i != res.end(); ++i)
        cout << *i << endl;
    return 0;
}
