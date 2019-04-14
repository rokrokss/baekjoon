#include <iostream>
#include <cmath>
using namespace std;

bool in(int x, int y, int cx, int cy, int r){
	int dx = cx-x;
	int dy = cy-y;
	double d = sqrt(dx*dx+dy*dy);
	if (d<r){
		return true;
	} else if (d>r){
		return false;
	}
}

int main() {
	int n;
	cin>>n;
	for (int i=0;i<n;i++){
		int x1, y1, x2, y2;
		cin >> x1 >> y1 >> x2 >> y2;
		int n1;
		cin >> n1;
		int hit = 0;
		for (int j=0;j<n1;j++){
			int cx, cy, r;
			cin >> cx >> cy >> r;
			bool A = in(x1, y1, cx, cy, r);
			bool B = in(x2, y2, cx, cy, r);
			if ((A||B)&&!(A&&B)){
				hit++;
			}
		}
		cout << hit << endl;
	}
	return 0;
}