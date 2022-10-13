/*
WORD-COMPOSITION(S, K)
let D be an empty dictionary (of strings and integers)
n <- |S|
i <- 1
while i <= n - K do
    if S[i,...,i + K] is not in D then
        D[S[i,...,i + K]] <- 0
        i <- i + 1
    else
        D[S[i,...,i + K]] <- D[S[i,...,i + K]] + 1
        i <- i + 1
let A be a list of keys of D
sort A
let R be an empy dictionary (of strings and integers)
for element in A do
    R[element] <- D[element]
return R
*/


#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;

map<string, int> word_composition(string s, int k) {
    map<string, int> D;
    int n = s.length();
    int i = 0;
    vector<string> A;
    while (i <= n - k) {
        string subs = s.substr(i, k);
        if (D.find(subs) != D.end()) {
            D[subs] = D[subs] + 1;
            i = i + 1;
        }
        else {
            D[subs] = 1;
            A.push_back(subs);
            i = i + 1;
        }
    }
    sort(A.begin(), A.end());
    map<string, int> R;
    for (auto e : A)
        R[e] = D[e];
    return R;
}

int main() {
    string s;
    int k;
    cin >> s >> k;
    map<string, int> res = word_composition(s, k);
    for (auto pair : res)
        cout << pair.first << " " << pair.second << endl;
    return 0;
}
