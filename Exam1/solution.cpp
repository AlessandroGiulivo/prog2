/*
WORD-COMPOSITION(s, k)
    n = |s|
    let D be an empty dictionary (of strings and integers)
    for i = 1 to n - k + 1 do
        w = s[i,...,i+k-1]
        if w in D then
            D[w] = D[w] + 1
        else
            D[w] = 1
    sort D
    let L be and empty list (of pairs of string and integer)
    for all w in D do
        append (w, D[w]) to L
    return L
*/


#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;

vector <pair <string, int> > word_composition(string s, int k) {
    int n = s.length();
    map<string, int> D;
    for (int i = 0; i <= n - k + 1; i++) {
        string w = s.substr(i, k - 1);
        if (D.find(w) != D.end()) {
            D[w] = D[w] + 1;
        }
        else {
            D[w] = 1;
        }
    }
    vector <pair <string, int> > L;
    for (auto w : D) {
        L.push_back(make_pair(w, D[w]));
    return L;
    }
}

int main() {
    string s;
    int k;
    cin >> s >> k;
    vector <pair <string, int> > result = word_composition(s, k);
    for (auto pair : result)
        cout << pair.first << " " << pair.second << endl;
    return 0;
}
