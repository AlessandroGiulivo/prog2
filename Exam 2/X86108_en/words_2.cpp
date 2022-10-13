/*
WORDS-2(n, A)
sort A
if n = 0 then
    return a list containing an empty string
else
    L = WORDS-2(n - 1, A)
    let L1 be and empty list
    for all e in L do
        for all c in A do
            concatenate e, c and append to L1
    return L1
*/


#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
using namespace std;


vector<string> words_2(int n, vector<char> A) {
    sort(A.begin(), A.end());
    if (n == 0) {
        vector<string> L(1);
        return L;
    }
    else {
        vector<string> L = words_2(n - 1, A);
        vector<string> L1;
        for (auto e : L) {
            for (auto c : A) {
                L1.push_back(e + c);
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
    vector<char> A;
    char x;
    while (ss >> x) A.push_back(x);
    
    vector<string> res = words_2(n, A);
    for (auto w : res) {
        cout << w << endl;
    }
    return 0;
}
