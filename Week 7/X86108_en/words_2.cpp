/*
WORDS-2(n, abc)
sort abc
if n = 0 then
    return a list containing an empty string
else
    L = WORDS-2(n - 1, abc)
    let L1 be and empty list
    for e in L do
        for c in abc do
            string <- c + e
            append string to L1
    return L1
*/


#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
using namespace std;


vector<string> words_2(int n, vector<char> abc) {
    sort(abc.begin(), abc.end());
    if (n == 0) {
        vector<string> L(1);
        return L;
    }
    else {
        vector <string> L = words_2(n - 1, abc);
        vector<string> L1;
        for (auto e : L) {
            for (auto c : abc) {
                string str = c + e;
                L1.push_back(str);
            }
        }
        return L1;
    }
}



int main() {
    string s;
    getline(cin, s);
    int n = stoi(s);
    
    getline(cin, s);
    istringstream ss(s);
    vector<char> abc;
    char x;
    while (ss >> x) abc.push_back(x);
    
    vector<string> res = words_2(n, abc);
    for (auto w : res) {
        cout << w << endl;
    }
    return 0;
}
