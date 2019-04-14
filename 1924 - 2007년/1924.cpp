#include <iostream>
#include <algorithm>
using namespace std;


int main() {
	int m, d;
	cin >> m >> d;
	int n=0;
	int r;
	for (int i=1;i<m;i++){
		if (i==1||i==3||i==5||i==7||i==8||i==10||i==12){
			n=n+31;
		}
		else if (i==2) {
			n = n + 28;
		}else{
			n=n+30;
		}
	}
	n=n+d-1;
	r=n%7;
	if(r==0){
		cout << "MON";
	}else if(r==1){
		cout << "TUE";
	}else if(r==2){
		cout << "WED";
	}else if(r==3){
		cout << "THU";
	}else if(r==4){
		cout << "FRI";
	}else if(r==5){
		cout << "SAT";
	}else if(r==6){
		cout << "SUN";
	}
	return 0;
}