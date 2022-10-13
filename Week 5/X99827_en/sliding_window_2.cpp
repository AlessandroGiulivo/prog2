/*
let A be an empty array
SLINDING-WINDOW(S, x, y)
n <- |S|
if n < x then
    do nothing
else if n = x then
    append S to A
else
    append S[0,...,x] to A
    S <- S[y,...,n]
    SLIDING-WINDOW(S, x, y) 
return A
*/

#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<string> A;
vector<string> sliding_window_2(string s, int x, int y) {
    vector<string> B;
    int n = s.length();
    if (n < x) {
        return A;
    }
    else if (n == x) {
        cout << s << endl;
        A.push_back(s);
    }
    else {
        cout << s.substr(0, x) << endl;
        A.push_back(s.substr(0, x));
        s = s.substr(y, n - y);
        sliding_window_2(s, x, y);
    }
    return B;
}

int main() {
    string s;
    int x;
    int y;
    cin >> s >> x >> y;
    vector<string> res = sliding_window_2(s, x, y);
    for (auto i = res.begin(); i != res.end(); ++i)
        cout << *i << endl;
    return 0;
}
