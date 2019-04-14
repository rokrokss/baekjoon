#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;


int main() {
	string s;
	getline(cin,s);
	int n=1;
	bool start = false;
	bool plus = false;
	bool zero = true;
	for (int i=0;i<s.length();i++){
		if (s[i]==' '){
			if(start) {
				plus = true;
			}
		}else{
			if (plus){
				n++;
				plus = false;
			}
			start = true;
			zero = false;
		}
	}
	if (zero){
		cout << 0;
	}else {
		cout << n;
	}
	return 0;
}