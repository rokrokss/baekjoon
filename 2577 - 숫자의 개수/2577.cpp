#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;


int main() {
	int A, B, C;
	cin >> A >> B >> C;
	int result[10] = {0};
	for (int i=0;i<10;i++){
		result[i]=0;
	}
	int S = A*B*C;
	if (S>100000000){ //9
		for (int i=0;i<9;i++){
			int a = S%10;
			result[a]++;
			S = S/10;
		}
	}else if(S>10000000){ //8
		for (int i=0;i<8;i++){
			int a = S%10;
			result[a]++;
			S = S/10;
		}
	}else{ //7
		for (int i=0;i<7;i++){
			int a = S%10;
			result[a]++;
			S = S/10;
		}
	}
	for (int i=0;i<10;i++){
		cout << result[i] << endl;
	}
	return 0;
}