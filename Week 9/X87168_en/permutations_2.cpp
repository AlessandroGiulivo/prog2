/*
PERMUTATIONS(S)
let L be an empty set (of strings)
    if |S| = 1 then
        append s to L
    else
        for i = 1 to |S| do
            for all t in PERMUTATIONS(S[2],..,S[|S|]) do
                append S[i], t to L
    return L
*/


#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <string>
using namespace std;


set<string> permutations_2(string s) {
    set<string> l;
    if (s.length() == 1) {
        l.insert(s);
    }
    else {
        for (int i = 0; i < s.length(); i++) {
            for (auto t : permutations_2(s.substr(0, i) + s.substr(i + 1, s.length() - i + 1))) {
                l.insert(s[i] + t);
            }
        }
    }
    return l;
}


int main() {
    string s;
    cin >> s;
    set<string> res = permutations_2(s);
    for (auto w : res) {
        cout << w << endl;
    }
    return 0;
}
