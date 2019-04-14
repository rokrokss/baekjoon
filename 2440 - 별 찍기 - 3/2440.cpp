#include <iostream>
#include <algorithm>
using namespace std;


int main() {
	int N;
	cin >> N;
	for(int i=0;i<N;i++){
		for(int j=N-i;j>0;j--){
			printf("*");
		}
		printf("\n");
	}
	return 0;
}