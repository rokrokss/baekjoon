#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

char ary[3072*6][3072];

void addstar(int k, int x, int y){
	if(k==0){
		ary[x][y]='*';
		ary[x+1][y+1]='*';
		ary[x-1][y+1]='*';
		ary[x+2][y+2]='*';
		ary[x+1][y+2]='*';
		ary[x][y+2]='*';
		ary[x-1][y+2]='*';
		ary[x-2][y+2]='*';
	}
	else {
		addstar(k-1,x,y);
		addstar(k-1,x-(3*pow(2,k-1)),y+3*pow(2,k-1));
		addstar(k-1,x+(3*pow(2,k-1)),y+3*pow(2,k-1));
	}
}

int main() {
	int N;
	cin >> N;
	int a; //2^k
	a = N/3;
	int hor = 2*N-1;
	int ver = N;
	for (int i=0;i<ver;i++) {
		for (int j = 0; j < hor; j++) {
			ary[j][i] = ' ';
		}
	}
	int sx, sy;
	sx = N-1;
	sy = 0;
	int k = (int)(log(a)/log(2));
	addstar(k, sx, sy);
	for (int i=0;i<ver;i++){
		for (int j=0;j<hor;j++){
			printf("%c", ary[j][i]);
		}
		printf("\n");
	}
	return 0;
}