#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;


int main() {
	int* ary = new int[8];
	for(int i=0;i<8;i++){
		cin >> ary[i];
	}
	bool start = false;
	bool as = false;
	bool des = false;
	bool mixed = false;
	for(int i=1;i<8;i++){
		if(ary[i]!=ary[i-1]&&!start){
			start = true;
		}
		if(start){
			if(ary[i]>ary[i-1]){
				as = true;
			}else if(ary[i]<ary[i-1]){
				des = true;
			}
		}
	}
	if (as&&des){
		cout << "mixed";
	}else if (as){
		cout << "ascending";
	}else if (des){
		cout << "descending";
	}else {
		cout << "mixed";
	}
	return 0;
}