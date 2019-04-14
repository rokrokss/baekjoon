#include <iostream>
#include <math.h>
#include <cmath>
using namespace std;

void t(double x1, double y1, double r1, double x2, double y2, double r2){
	double d;
	double d1 = x2-x1;
	double d2 = y2-y1;
	d = sqrt(d1*d1+d2*d2);
	double r = r2+r1;
	double rr = abs(r2-r1);
	if (d == 0 && rr==0){
		cout << -1 << endl;
	}else if (d > r){
		cout << 0 << endl;
	}else if (d == r){
		cout << 1 << endl;
	} else if (d<r && rr<d){
		cout << 2 << endl;
	} else if (rr == d){
		cout << 1 << endl;
	} else {
		cout << 0 << endl;
	}
}

int main() {
	int n;
	cin>>n;
	for (int i=0;i<n;i++){
		int x1, y1, r1, x2, y2, r2;
		cin>>x1>>y1>>r1>>x2>>y2>>r2;
		t(x1, y1, r1, x2, y2, r2);
	}
	return 0;
}