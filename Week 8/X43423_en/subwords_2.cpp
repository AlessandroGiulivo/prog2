/*
SUBWORDS-2(S)
S1, S2 = SUBWORDS-2(s, 1)
sort S2
return S2
SUBWORDS-2(S, i)
if i > |s| then 
    return {}, {}
else
    S1, S2 = SUBWORDS-2(s, i + 1)
    insert an empty string in S1
    let SS1 be an empty set (of strings)
    for all w in S1 do
        insert s[i] + w in SS1
        insert s[i] + w in S2
    return SS1, S2
*/


#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <iterator>
#include <utility>
#include <string>
using namespace std;


pair<set<string>, set<string>> subwords_2(string s,int i) {
    if ( i >= s.length()) {
        pair<set<string>, set<string>> p {{}, {}};
        return p;
    }
    else {
        pair<set<string>, set<string>> p1;
        p1 = subwords_2(s, i + 1);
        set<string> s1 = p1.first;
        set<string> s2 = p1.second;
        s1.insert("");
        set<string> ss1;
        for (auto w : s1) {
            ss1.insert(s[i] + w);
            s2.insert(s[i] + w);
        }
        pair<set<string>, set<string>> p2 {ss1, s2};
        return p2;
    }
}
set<string> subwords_2(string s) {
    pair<set<string>, set<string>> p3;
    p3 = subwords_2(s, 0);
    set<string> s3 = p3.second;
    return s3;
}


int main() {
    string s;
    cin >> s;
    set<string> res = subwords_2(s);
    for (auto w : res) {
        cout << w << endl;
    }
    return 0;
}
