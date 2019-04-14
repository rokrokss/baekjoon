#include <iostream>
#include <math.h>
using namespace std;



int main() {
	int t;
	cin >> t;
	for (int i=0;i<t;i++){
		int H, W, N;
		cin >> H >> W >> N;
		int Y, X;
		if (N%H==0){
			X=N/H;
		}
		else {
			X=N/H+1;
		}
		Y=N%H;
		if(Y==0){
			Y=H;
		}
		int answer = 100*Y+X;
		cout << answer << endl;
	}
	return 0;
}