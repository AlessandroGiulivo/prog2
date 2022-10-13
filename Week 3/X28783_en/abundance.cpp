/*
ABUNDANCE(S)
    let D be an empty dictionary (of strings to numbers)
    for string in S do
        let c_string be an empty string
        for character in reversed(string) do
            if character == A then
                append T to c_string
            else if character == T then
                append A to c_string
            else if character == C then
                append G to c_string
            else if character == G then
                append C to c_string
        if string in keys of D then
            D[string] += 1
        else if c_string in keys of D then
            D[c_string] += 1
        else 
            if string < c_string then        --- order alphabetically
                D[string] = 1
            else 
                D[c_string] = 1
    return each key and its value of the sorted D
*/

#include <iostream>
#include <string>
#include <map>
#include <set>
using namespace std;

int main() {
     map<string, int> D
