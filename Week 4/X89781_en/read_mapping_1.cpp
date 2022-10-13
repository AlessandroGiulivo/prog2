/*
READ-MAPPING-1(S)
    let D be an empty dictionary (of strings and integers)
    for i = 0 to i = |S| - 1 do
        D[S[i,...,|s|]] = i
    let A be an empty array (of integers)
    i <- 0
    for x in D do
        i <- i + 1
        A[i] <- x
    sort A
    for suffix in A do
        return D[suffix]
*/


#include <iostream>
#include <string>
#include <map>
#include <set>
using namespace std;

int main() {
    map<string, int> D;
    string s;
    cin >> s;
    int n = s.length();
    int i = 1;
    string A[n];
    while (i <= n-1) {
        i = i + 1;
        D[s.substr(i, n - i)] = i;
    }
    i = 0;
    while (i <= n - 1) {
        A[i] = D[i];0
        i = i + 1;
    }
    for (i = 0; i < n; i++) {
        cout << A[i] << endl;
    }
return 0;
}


