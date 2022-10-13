/*
This program will take a DNA string as input, and return the first ORF within the string

PSEUDOCODE

GENE_FINDING(s)
    Let stop codons be a list of strings
    Let orf be and empty string
    stop_codons <- ["TGA", "TAG", "TAA"]
    s <- s[s.find('ATG'):]
    for stop_codon in stop_codons do
        for i = 0 to i = |s| every 3 numbers do
            if s[i:i+3] = stop_codon then
                orf <- s[:i+3]
    return orf
*/

#include <iostream>
#include <string>
using namespace std;

int main() {
	string inp;
	cin >> inp;
	for (int i = 0; i < (inp.length()-3) ; i++){
		if (inp.substr(i,3) == "ATG"){
			string ns = inp.substr(1,inp.length());
			for (int j = +3; j < inp.length()-3 ; j+=3){
				if (inp.substr(j,3) == "TAG" or inp.substr(j,3) == "TAA" or inp.substr(j,3) == "TGA"){
					int end = j+3;
					cout << inp.substr(i,end) << endl;
					break;
				}
			}
			break;
		}
	}	
return(0);
}
