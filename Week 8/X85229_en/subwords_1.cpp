/*
SUBWORDS-1(S)
let T be an empty set (of strings)
for i = 1 to |S| do                      --- for (int i = 0; i < s.length(); i++)
    for j = i to |S| do                  --- for (int j = i; j < s.length(); j++)
        insert s[i,...,j] in S           --- s[i:j+1]   ---s.substr(i, j - i + 1)
let L be an empty list (of strings)
for all w in S do
    append w to L
sort L
return L
*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <iterator>
using namespace std;


vector<string> subwords_1(string s) {
    set<string> T;
    for (int i = 0; i < s.length(); i++) {
        for (int j = i; j < s.length(); j++) {
            T.insert(s.substr(i, j - i + 1));
        }
    }
    vector<string> L;
    for (auto w : T) {
        L.push_back(w);
    }
    sort(L.begin(), L.end());
    return L;
}


int main() {
    string s;
    cin >> s;
    vector<string> res = subwords_1(s);
    for (auto w : res) {
        cout << w << endl;
    }
    return 0;
}
