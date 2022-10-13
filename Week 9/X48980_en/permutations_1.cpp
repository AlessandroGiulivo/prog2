/*
PERMUTATIONS(S)
    let T be an empty stack (of characters)
    for i = 1 to |S| do
        push s[i] onto T
    let L be an empty set (of strings)
    insert an empty string in L
    while T is not empty do
        pop from T the top element x
        let L' be an empty set (of strings)
        for all w in L do
            for i = 1 to |w| + 1 do
                insert w[1,...,i - 1] + x + w[i,...,|w|] in L'
        L = L'
    sort L
    return L
*/


#include <iostream>
#include <vector>
#include <set>
#include <stack>
using namespace std;


set<string> permutations_1(string s) {
    stack<string> t;
    for (int i = 0; i < s.length(); i++) {
        t.push(s.substr(i, 1));
    }
    set<string> l;
    l.insert("");
    while (!t.empty()) {
        string x = t.top();
        t.pop();
        set<string> l1;
        for (auto w : l) {
            for (int i = 0; i <= w.length(); i++) {
                l1.insert(w.substr(0, i) + x + w.substr(i, w.length() - i));
            }
        }
        l = l1;
    }
    return l;
}


int main() {
    string s;
    cin >> s;
    set<string> res = permutations_1(s);
    for (auto w : res) {
        cout << w << endl;
    }
    return 0;
}
