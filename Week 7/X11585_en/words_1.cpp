/*
WORDS-1(n, abc)
sort abc
let L be a list containing an empty string
s <- 0
while s < n do
    let L1 be and empty list
    for e in L do
        for c in abc do
            str <- c + e
            append str to L1
    s <- s + 1
    L <- L1
return L
*/


#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
using namespace std;

vector<string> words_1(int n, vector<char> abc) {
    sort(abc.begin(), abc.end());
    vector<string> L(1);
    int s = 0;
    while (s < n) {
        vector<string> L1;
        for (auto e : L) {
            for (auto c : abc) {
                string str = c + e;
                L1.push_back(str);
            }
        }
    s = s + 1;
    L = L1;
    }
return L;
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
    
    vector<string> res = words_1(n, abc);
    for (auto w : res) {
        cout << w << endl;
    }
    return 0;
}
