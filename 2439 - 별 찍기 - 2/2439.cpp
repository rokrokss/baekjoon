#include <iostream>
#include <algorithm>
using namespace std;


int main() {
	int N;
	cin >> N;
	for(int i=1;i<=N;i++){
		for(int j=0; j<N-i;j++){
			printf(" ");
		}
		for(int j=0; j<i;j++){
			printf("*");
		}
		printf("\n");
	}
	return 0;
}